# -*- coding: utf-8 -*-
""" Script to crawl Article from vox.com

vox
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CVoxCrawler(BaseCrawler):
    start_urls = [
        'https://www.vox.com/marijuana-legalization',
    ]

    # source = 'Vox'
    source_id = 'vox'

    config_selectors = {

        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.c-entry-box--compact__title > a::attr(href)',
        'NEXT_PAGE_URL': '.c-pagination__more::attr(href), .c-pagination__next::attr(href)',  # default

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '.c-entry-content',

    }


if __name__ == "__main__":
    crawler = CVoxCrawler()
    crawler.run()