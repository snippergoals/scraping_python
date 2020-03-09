# -*- coding: utf-8 -*-
""" Script to crawl Article from westword.com

denver-westworld
"""
import json
from scrapy.selector import Selector

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CDenverWestworldCrawler(BaseCrawler):
    start_urls = [
        'https://www.westword.com/marijuana',
        'https://www.westword.com/marijuana/tocAjax?page=1'
    ]

    # source = 'Denver Westworld'
    source_id = 'denver-westworld'

    config_selectors = {

        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.headline::attr(href)',
        # 'NEXT_PAGE_URL': '.pager-next > a::attr(href)',  # default

        # Css selector on article's detail page (the page display full content of article)
        # 'ARTICLE_PUBLISHED_AT': 'story-body ',
        'ARTICLE_AUTHOR': '.byline a::text',
        'ARTICLE_CONTENT': '.story-body > p',
    }

    # override 
    def extract_post_urls(self, selector, html):
        post_urls = super(CDenverWestworldCrawler, self).extract_post_urls(selector, html)
        if len(post_urls) == 0:
            jo = json.loads(html)
            sel = Selector(text=jo['data'])
            post_urls = super(CDenverWestworldCrawler, self).extract_post_urls(sel, html)
        return post_urls
    
    # override 
    def extract_next_page_url(self, selector, html, url):
        post_urls = self.extract_post_urls(selector, html)
        if len(post_urls) > 3 and '?page=' in url:
            page = url.split('?page=')[-1].split('&')[0]
            page = int(page) + 1
            return 'https://www.westword.com/marijuana/tocAjax?page={0}'.format(page)
        return None

if __name__ == "__main__":
    crawler = CDenverWestworldCrawler()
    crawler.run()