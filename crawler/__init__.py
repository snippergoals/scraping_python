# -*- coding: utf-8 -*-
import requests
import requests_cache
from pymongo import MongoClient
import json
import demjson
import logging
import traceback
from scrapy.selector import Selector
from urllib.parse import urljoin
from scrapely.extractors import text, htmlregion
import os
import re
from dateutil import parser
from datetime import datetime
try:
    from .smmry_client import SMMRYClient
except:
    from smmry_client import SMMRYClient

"""
    This class is parent class of all Crawler
    Each website we need 1 crawler which inherite this class
    ex: class CCannabisWatchCrawler(BaseCrawler):
"""
class BaseCrawler(object):
    start_urls = []

    source_id = None
    source_name = None
    source = None
    config_selectors = {
        # 'POST_URLS': '',
        # 'NEXT_PAGE_URL': '',
        # 'ARTICLE_CONTENT': '',
        # 'ARTICLE_AUTHOR': '',
    }

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.NewsAPI
        self.collection = self.db.Articles
        self.crawler_env = os.environ.get("NEWS_API_CRAWLER_ENV", "dev")
        self.s = SMMRYClient()

        if self.crawler_env == 'dev':
            requests_cache.install_cache('crawler_cache')

    def extract_title(self, selector):
        """
            Extract title of article
            @param selector Scrapy.Selector object (https://docs.scrapy.org/en/latest/topics/selectors.html)

            @return Text title of article, return None if not found
        """
        css = self.config_selectors.get('ARTICLE_TITLE')
        if css is not None:
            v = selector.css(css).extract_first('').strip()
        else:
            v = selector.css('meta[property="og:title"]::attr(content)').extract_first()
        
        # clean data
        if v is not None:
            v = v.split('|')[0].strip()
            v = v.split(' - ')[0].strip()
        return v

    def extract_author(self, selector):
        """
            Extract author of article
            @param selector Scrapy.Selector object (https://docs.scrapy.org/en/latest/topics/selectors.html)

            @return Text author of article, return None if not found
        """

        css = self.config_selectors.get('ARTICLE_AUTHOR')
        if css is not None:
            v = u' '.join(selector.css(css).extract()).strip()
        else:
            v = selector.css('[itemprop="author"] [itemprop="name"]::attr(content)').extract_first()
        if v is not None:
            v = re.sub(r'\s+', ' ', v)
        return v            

    def extract_published_at(self, selector):
        """
            Extract published date of article
            @param selector Scrapy.Selector object (https://docs.scrapy.org/en/latest/topics/selectors.html)

            @return Text Published date of article, return None if not found
        """
        css = self.config_selectors.get('ARTICLE_PUBLISHED_AT')
        if css is not None:
            v = selector.css(css).extract_first('').strip()
        else:
            v = selector.css('meta[property="article:published_time"]::attr(content)').extract_first()
        return v

    def extract_source(self):
        """
            Extract source of article
            if source_name is set then use it, if not then use source

            @return Text source of article
        """
        source_id = self.source_id if self.source_id is not None else None
        return source_id

    def extract_url_to_image(self, selector):
        """
            Extract image of article
            @param selector Scrapy.Selector object (https://docs.scrapy.org/en/latest/topics/selectors.html)

            @return Text image of article, return None if not found
        """
        css = self.config_selectors.get('ARTICLE_URL_TO_IMAGE')
        if css is not None:
            v = selector.css(css).extract_first('').strip()
        else:
            v = selector.css('meta[property="og:image"]::attr(content)').extract_first()
        return v

    def extract_description(self, selector):
        """
            Extract description of article
            @param selector Scrapy.Selector object (https://docs.scrapy.org/en/latest/topics/selectors.html)

            @return Text Description of article, return None if not found
        """
        css = self.config_selectors.get('ARTICLE_DESCRIPTION')
        if css is not None:
            desc = selector.css(css).extract_first('').strip()
        else:
            desc = selector.css('meta[property="og:description"]::attr(content)').extract_first('').strip()
            if desc == '':
                desc = selector.css('meta[name=description]::attr(content)').extract_first('').strip()
        return desc

    def extract_content(self, selector):
        """
            Extract Content of article
            @param selector Scrapy.Selector object (https://docs.scrapy.org/en/latest/topics/selectors.html)

            @return Text Content of article, return None if not found
        """
        t = lambda s: text(htmlregion(s))
        content = u' '.join(selector.css(self.config_selectors.get('ARTICLE_CONTENT')).extract())
        return t(content)

    def extract_post_urls(self, selector, html):
        """
            Extract post urls from list page
            @param selector Scrapy.Selector object (https://docs.scrapy.org/en/latest/topics/selectors.html)
            @param html Text Content of webpage

            @return List List of urls
        """
        return selector.css(self.config_selectors.get('POST_URLS')).extract()

    def extract_next_page_url(self, selector, html, url):
        """
            Extract next_page_url from list page
            @param selector Scrapy.Selector object (https://docs.scrapy.org/en/latest/topics/selectors.html)
            @param html Text Content of webpage
            @param url Url of webpage

            @return The next page url, None if not found
        """
        next_page_url = None
        if self.config_selectors.get('NEXT_PAGE_URL') is not None:
            next_page_url = selector.css(self.config_selectors.get('NEXT_PAGE_URL')).extract_first()
        if next_page_url is None:
            next_page_url = selector.css('link[rel=next]::attr(href)').extract_first()
    
        if next_page_url is not None:
            next_page_url = urljoin(url, next_page_url)

        return next_page_url  

    def parse_article(self, response, url):
        """
            Extract article from webpage
            @param reponse Scrapy.Response
            @param url Url of webpage
            @return Dict An key-value dict of article
        """
        logging.info('Parsing article: ' + url)
        sel = Selector(text=response.text)

        article = {
            'title': self.extract_title(sel),
            'url': url,
            'description': self.extract_description(sel),
            'author': self.extract_author(sel),
            'publishedAt': self.extract_published_at(sel),
            'content': self.extract_content(sel),
            'source_id': self.extract_source(),
            'urlToImage': self.extract_url_to_image(sel)
        }

        for script in sel.css('script[type="application/ld+json"]::text').extract():
            try:
                try:
                    jo = demjson.decode(script.strip())
                except:
                    # correct the invalid json format
                    script = re.sub(r'"\s*:\s*"(.*?)"\s*(,\s*"|})', self.json_correct, script)
                    jo = demjson.decode(script.strip())

                if '@type' in jo and jo['@type'] ==  "NewsArticle":
                    article['publishedAt'] = article['publishedAt'] or jo.get('datePublished')
                    article['description'] = article['description'] or jo.get('description')
                    article['title'] = article['title'] or jo.get('headline')
                    if article['author'] == '' or article['author'] is None:
                        tmp = jo.get('author', {})
                        if isinstance(tmp, list):
                            if len(tmp) > 0:
                                article['author'] = tmp[0].get('name')
                        else:
                            article['author'] = tmp.get('name')

                    if article['urlToImage'] == '' or article['urlToImage'] is None:
                        tmp = jo.get('image', {})
                        if isinstance(tmp, list):
                            if len(tmp) > 0:
                                article['urlToImage'] = tmp[0]
                        else:
                            article['urlToImage'] = tmp.get('url')

                    if 'articleBody' in jo:
                        article['content'] == jo['articleBody']

            except Exception as ex:
                logging.warning("Exception in parse_article -  demjson.decode: {0}\n{1}".format(url, ex))

                if article['publishedAt'] is None and '"datePublished": "' in script:
                    article['publishedAt'] = script.split('"datePublished": "')[1].split('"', 1)[0].strip()
                
                if article['author'] is None and '"author":' in script and '"name": "' in script.split('"author":')[1]:
                    article['author'] = script.split('"author":')[1].split('"name": "', 1)[1].split('"', 1)[0].strip()

        return article
        
    def parse_posts(self, response, url):
        """
            Extract posts (links to articles) from search result page or home page
            @param reponse Scrapy.Response
            @param url Url of result webpage
            
            @return Set A set of article's url and next page url
        """
        logging.info('Parsing posts page: ' + url)
        sel = Selector(text=response.text)
        post_urls = [urljoin(url, href) for href in self.extract_post_urls(sel, response.text)]
        next_page_url = self.extract_next_page_url(sel, response.text, url)

        return post_urls, next_page_url

    def process_posts_page(self, url):
        """
            Get an url make request to get content then call parse_posts
            @param url Url of webpage
            @return Set A set of article's url and next page url
        """
        try:
            if url not in self.crawled:
                response = self._http_get(url)
                if response is not None:
                    post_urls, next_page_url = self.parse_posts(response, url)
                    if self.crawler_env == 'daily' and\
                        next_page_url is not None and len(post_urls) > 0 and\
                        self.mongodb_check_exists(post_urls[-1]):
                        next_page_url = None
                    return post_urls, next_page_url
        except Exception as ex:
            logging.error("Exception in process_posts_page: {0}".format(url))
            traceback.print_exc()
        return [], None

    def process_article_page(self, url):
        """
            Get an url make request to get content then call parse_article
            @param url Url of article 
            @return Dict An key-value dict of article
        """
        try:
            if not self.mongodb_check_exists(url) and url not in self.crawled:
                response = self._http_get(url)
                if response is not None:
                    return self.parse_article(response, url)
        except Exception as ex:
            logging.error("Exception in process_posts_page: {0}".format(url))
            traceback.print_exc()
        return None

    def save_to_mongodb(self, article, url=''):
        """
            Save an article into db
            @param article An key-value dict of article
        """
        try:
            if article is not None and article.get('title'):
                if 'publishedAt' in article and article['publishedAt'] is not None and not isinstance(article['publishedAt'], datetime):
                    try:
                        article['publishedAt'] = parser.parse(article['publishedAt'])
                    except:
                        logging.warning('Date parse exception: {0}'.format(article['publishedAt']))
                        article['publishedAt'] = None
                if 'summarization' not in article:
                    article['summarization'] = self.s.summarization_by_content(article['content'])

                if article is not None and type(article) is dict:
                    logging.info('Inserting to mongodb: {0}'.format(article.get('title', '')))
                    if 'source_id' not in article:
                        article['source_id'] = self.source_id
                    self.collection.insert_one(article)
                else:
                    logging.info('Inserting to mongodb: {0}'.format(article))
            else:
                logging.warning('Ignore None article: {0}'.format(url))
        except Exception as ex:
            logging.error("Exception in save_to_mongodb")
            traceback.print_exc()

    def mongodb_check_exists(self, url):
        """
            Check if an article is already crawled or not
            @param url Text Url of article
            @return Boolean True - False
        """
        try:
            return self.collection.find_one({'url': url}) is not None
        except Exception as ex:
            logging.error("Exception in mongodb_check_exists: {0}".format(url))
            traceback.print_exc()

    def json_correct(self, match):
        """
            function used to correct invalid json string
        """
        return u'": "{0}"{1}'.format(match.group(1).replace('"', '\\"'), match.group(2))

    crawled = []
    def _http_get(self, url):
        """
            Make a web request to get content of webpage
            @param url Url of webpage
            @return Text  The content of webpage
        """
        # custome header
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive'
        }

        if url not in self.crawled:
            self.crawled.append(url)

        try:
            response = requests.get(url, headers=headers)
            logging.info("HTTP GET: {0} - {1}".format(response.status_code, url))
            print("HTTP GET: {0} - {1}".format(response.status_code, url))
            return response
        except Exception as ex:
            logging.error("Exception in _http_get: {0}".format(url))
            traceback.print_exc()
        
        return None

    def run(self):
        """
            Main method to call to crawl all article
        """
        for url in self.start_urls:
            for page in range(0, 10000): # 10,000 page  as maximun
                _post_urls, next_page_url = self.process_posts_page(url)
                for post_url in _post_urls:
                    article = self.process_article_page(post_url)
                    if article is not None:
                        self.save_to_mongodb(article, post_url)
                url = next_page_url
                if next_page_url is None:
                    break
            
    def test_article(self, url):
        """
            Use for development only
            To test the config_selectors
        """
        print(json.dumps(self.process_article_page(url)))

    def quick_test(self):
        """
            Use for development only
            To test the a crawler
        """

        post_urls = []
        for url in self.start_urls:
            _post_urls, next_page_url = self.process_posts_page(url)
            print("----------")
            print("Testing start_url: {0}".format(url))
            print("\tpost_urls > 0: \t\t{0}".format(len(_post_urls) > 0))
            print("\tnext_page_url # None: \t{0}".format(next_page_url is not None))

            if len(_post_urls) > 0:
                post_urls.append(_post_urls[0])
            if len(_post_urls) > 1:
                post_urls.append(_post_urls[-1])

            if next_page_url is not None:
                _post_urls, next_page_url = self.process_posts_page(next_page_url)
                print("----------")
                print("Testing next_page_url: {0}".format(next_page_url))
                print("\tpost_urls > 0: \t\t{0}".format(len(_post_urls) > 0))
                print("\tnext_page_url # None: \t{0}".format(next_page_url is not None))

                if len(_post_urls) > 0:
                    post_urls.append(_post_urls[0])
                if len(_post_urls) > 1:
                    post_urls.append(_post_urls[-1])
        
        article = None
        for post_url in set(post_urls):
            article = self.process_article_page(post_url)
            print("----------")
            print("Testing article: {0}".format(post_url))
            mess = None
            if article is not None:
                mess = ''
                for k in article:
                    if article[k] is None or article[k] == '':
                        mess += '{0}={1} '.format(k, article[k])
            if mess == '':
                mess = 'OK'
            # self.save_to_mongodb(article, post_url)
            print("\tArticle is OK ?: {0}".format(mess))

        print(json.dumps(article))