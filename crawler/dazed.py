# -*- coding: utf-8 -*-
""" Script to crawl Article from dazeddigital.com

dazed
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CDazedCrawler(BaseCrawler):
    start_urls = [
        'https://www.dazeddigital.com/tag/cannabis',
        'https://www.dazeddigital.com/tag/weed',
        'https://www.dazeddigital.com/tag/marijuana'
    ]

    # source = 'Dazed'
    source_id = 'dazed'

    config_selectors = {

        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.article-list-item-link > a::attr(href)',
        'NEXT_PAGE_URL': 'a.article-list-load-more::attr(href)',  # default

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '.article-body',
    }


if __name__ == "__main__":
    crawler = CDazedCrawler()
    crawler.run()