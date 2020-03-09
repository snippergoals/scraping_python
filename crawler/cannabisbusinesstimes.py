# -*- coding: utf-8 -*-
""" Script to crawl Article from cannabisbusinesstimes.com

cannabis-business-times
"""
import json
import logging
from urllib.parse import urljoin
try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler



class CCannabisBusinessTimesCrawler(BaseCrawler):
    start_urls = [
        'https://www.cannabisbusinesstimes.com/news/category/interviews-opinion/',
        'https://www.cannabisbusinesstimes.com/news/category/legislation-and-regulation/',
        'https://www.cannabisbusinesstimes.com/keyword/compliance/',
        'https://www.cannabisbusinesstimes.com/keyword/dispensary/',
        'https://www.cannabisbusinesstimes.com/keyword/canada/',
        'https://www.cannabisbusinesstimes.com/keyword/international/',
        'https://www.cannabisbusinesstimes.com/news/category/vendor-news/',
        'https://www.cannabisbusinesstimes.com/news/category/business-and-finance/',
        'https://www.cannabisbusinesstimes.com/news/category/grower-agriculture/',
        'https://www.cannabisbusinesstimes.com/news/category/medical/',
        'https://www.cannabisbusinesstimes.com/keyword/hemp/',
        'https://www.cannabisbusinesstimes.com/keyword/pesticides/',
        'https://www.cannabisbusinesstimes.com/news/category/politics/',
        'https://www.cannabisbusinesstimes.com/keyword/lighting/',
        'https://www.cannabisbusinesstimes.com/news/category/mergers-acquisitions/',
    ]

    # source = 'Cannabis Business Times'
    source_id = 'cannabis-business-times'

    config_selectors = {
         # Css selector on articles page (the page list many articles)
        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '#article-body',
        # 'ARTICLE_AUTHOR': '.byline ::text',

    }

    def getEndlessScroll(self, response):
        if 'Utilities.EndlessScroll' in response.text:
            url = response.text.split('Utilities.EndlessScroll', 1)[1].split('"', 4)[-2].strip()
            return urljoin(response.url, url)

        return None
    
    # override method
    def parse_posts(self, response, url):
        logging.info('Parsing posts page: ' + url)
        jo = json.loads(response.text)
        post_urls = []
        next_page_url = None
        for article in jo:
            post_url = article.get('Path') or article.get('SeoPath')
            if post_url:
                post_urls.append(urljoin(url, post_url))

        if len(post_urls) > 0:
            page = url.split('page=')[1].split('&')[0]
            page = int(page) + 1
            next_page_url = "{0}&page={1}".format(url.split('&page=')[0], page)

        return post_urls, next_page_url

    # override method
    def run(self):
        """
            Main method to call to crawl all article
        """
        for url in self.start_urls:
            response = self._http_get(url)
            if response is not None:
                url = self.getEndlessScroll(response)
                if url:
                    url = "{0}&page=0".format(url)
                    for page in range(0, 10000): # 10,000 page  as maximun
                        _post_urls, next_page_url = self.process_posts_page(url)
                        for post_url in _post_urls:
                            article = self.process_article_page(post_url)
                            if article is not None:
                                self.save_to_mongodb(article)
                        url = next_page_url
                        if next_page_url is None:
                            break

if __name__ == "__main__":
    crawler = CCannabisBusinessTimesCrawler()
    crawler.run()