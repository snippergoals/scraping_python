# -*- coding: utf-8 -*-
""" Script to crawl Article from fool.com

the-motley-fool
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CTheMotleyFoolCrawler(BaseCrawler):
    start_urls = [
        'https://www.fool.com/marijuana-stocks',
    ]

    # source = 'The Motley Fool'
    source_id = 'the-motley-fool'

    config_selectors = {

        # Css selector on articles page (the page list many articles)
        'POST_URLS': 'article h4 > a::attr(href)',
        
        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '.article-content',

    }


if __name__ == "__main__":
    crawler = CTheMotleyFoolCrawler()
    crawler.run()