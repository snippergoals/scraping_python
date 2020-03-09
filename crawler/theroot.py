# -*- coding: utf-8 -*-
""" Script to crawl Article from theroot.com

the-root
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CTheRootCrawler(BaseCrawler):
    start_urls = [
        'https://www.theroot.com/tag/cannabis',

    ]

    # source = 'The Root'
    source_id = 'the-root'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.entry-title > a::attr(href)',
        'NEXT_PAGE_URL': 'a[data-ga*="More stories click"]::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '.post__content-wrapper .post-content > p',
    }


if __name__ == "__main__":
    crawler = CTheRootCrawler()
    crawler.run()