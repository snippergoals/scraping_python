# -*- coding: utf-8 -*-
""" Script to crawl Article from firstpost.com

firstpost
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CFirstpostCrawler(BaseCrawler):
    start_urls = [
        'https://www.firstpost.com/tag/cannabis',
    ]

    # source = 'Firstpost'
    source_id = 'firstpost'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.articles-list > li > a::attr(href)',
        'NEXT_PAGE_URL': '[rel="next"]::attr(href)',  # default

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_AUTHOR': '.article-by::text',
        'ARTICLE_CONTENT': '.article-full-content',

    }
if __name__ == "__main__":
    crawler = CFirstpostCrawler()
    crawler.run()