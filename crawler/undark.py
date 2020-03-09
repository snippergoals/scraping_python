# -*- coding: utf-8 -*-
""" Script to crawl Article from undark.org

undark
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CUndarkCrawler(BaseCrawler):
    start_urls = [
        'https://undark.org/tag/marijuana',
        'https://undark.org/tag/cannabis',
    ]

    # source = 'Undark'
    source_id = 'undark'

    config_selectors = {

        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.entry-content > a::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_PUBLISHED_AT': 'h1.entry-title ~ div [pubdate]::attr(datetime)',
        'ARTICLE_AUTHOR': 'h1.entry-title ~ div [itemprop="author"]::text',
        'ARTICLE_CONTENT': '#wtr-content > p',

    }


if __name__ == "__main__":
    crawler = CUndarkCrawler()
    crawler.run()