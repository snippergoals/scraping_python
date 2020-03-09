# -*- coding: utf-8 -*-
""" Script to crawl Article from people.com

people-magazine
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CPeopleMagazineCrawler(BaseCrawler):
    start_urls = [
        'https://people.com/tag/marijuana',
    ]

    # source = 'People Magazine'
    source_id = 'people-magazine'

    config_selectors = {

        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.category-page-item-content > a::attr(href), .category-page-videos-link::attr(href)',
        # 'NEXT_PAGE_URL': '.pager-next > a::attr(href)',  # default

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_PUBLISHED_AT': '.published-date::text',
        'ARTICLE_AUTHOR': '.author-text .author-name::text',
        'ARTICLE_CONTENT': '.article-content-container > p, #article-body p',

    }


if __name__ == "__main__":
    crawler = CPeopleMagazineCrawler()
    crawler.run()