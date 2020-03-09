# -*- coding: utf-8 -*-
""" Script to crawl Article from complex.com

complex
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler
import json
from datetime import datetime

class CComplexCrawler(BaseCrawler):
    start_urls = [
        'https://www.complex.com/api/tag/2836/articles?take=10&skip=0', #https://www.complex.com/tag/marijuana',
        'https://www.complex.com/api/tag/15319/articles?take=10&skip=0' #'https://www.complex.com/tag/cannabis',
    ]

    # source = 'Complex'
    source_id = 'complex'

    config_selectors = {

        # Css selector on articles page (the page list many articles)
        'POST_URLS': 'a.gtm-article::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_PUBLISHED_AT': 'meta[property="article:published_time"]::attr(content), [itemprop="datePublished"]::text',
        'ARTICLE_AUTHOR': '[itemprop="author"] [itemprop="name"]::attr(content), [itemProp="author"] [itemProp="name"]::text',
        'ARTICLE_CONTENT': '.article-body',
    }

    def extract_post_urls(self, selector, html):
        """
            Extract post urls from list page
            @param selector Scrapy.Selector object (https://docs.scrapy.org/en/latest/topics/selectors.html)
            @param html Text Content of webpage

            @return List List of urls
        """
        post_urls = []
        jo = json.loads(html, strict=False)
        for article in jo:
            slug = article['properties']['renderChannel']['properties']['slug']
            alias = article['properties']['alias']
            date = datetime.fromtimestamp(int(article['properties']['datePublished'])/1000)
            url = 'https://www.complex.com/{}/{}/{:02}/{}'.format(slug, date.year, date.month, alias)
            if url not in post_urls:
                post_urls.append(url)
        return post_urls
    
    def extract_next_page_url(self, selector, html, url):
        jo = json.loads(html, strict=False)
        if len(jo) == 10:
            arr = url.split('&skip=')
            skip = int(arr[1]) + 10
            next_page_url = '{}&skip={}'.format(arr[0], skip)
            return next_page_url
        return None

if __name__ == "__main__":
    crawler = CComplexCrawler()
    crawler.run()