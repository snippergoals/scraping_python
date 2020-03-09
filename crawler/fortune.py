# -*- coding: utf-8 -*-
""" Script to crawl Article from fortune.com

fortune
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CFortuneCrawler(BaseCrawler):
    start_urls = [
        'http://fortune.com/tag/cannabis/',
    ]

    # source = 'Fortune'
    source_id = 'fortune'

    config_selectors = {
        'POST_URLS': '.article-info a::attr(href)',
        'ARTICLE_TITLE': 'h1.headline::text, h1.longform-headline::text',
        'ARTICLE_AUTHOR': '.author-text .author-name ::text',
        'ARTICLE_PUBLISHED_AT': '[data-content_published_date]::attr(data-content_published_date)',
        'ARTICLE_CONTENT': '#article-body .padded',
        'NEXT_PAGE_URL': '.pagination-next::attr(href)',
    }


if __name__ == "__main__":
    crawler = CFortuneCrawler()
    crawler.run()