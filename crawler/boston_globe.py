# -*- coding: utf-8 -*-
""" Script to crawl Article from bostonglobe.com

the-boston-globe
"""
import re
try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CTheBostonGlobeCrawler(BaseCrawler):
    start_urls = [
        'https://www.bostonglobe.com/marijuana',
    ]

    # source = 'The Boston Globe'
    source_id = 'the-boston-globe'

    config_selectors = {

        # Css selector on articles page (the page list many articles)
        'POST_URLS': '[href*="/news/marijuana"]::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '[class="article | rail"]',

    }

    # override
    def extract_post_urls(self, selector, html):
        urls = selector.css(self.config_selectors.get('POST_URLS')).extract()
        for url in re.findall(r'(\/news\/marijuana\/[^"]+)', html):
            url = url.strip('/')
            if url not in urls:
                urls.append(url)
        return urls


if __name__ == "__main__":
    crawler = CTheBostonGlobeCrawler()
    crawler.run()