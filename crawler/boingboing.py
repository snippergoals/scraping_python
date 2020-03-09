# -*- coding: utf-8 -*-
""" Script to crawl Article from boingboing.net

boing-boing
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CBoingBoingCrawler(BaseCrawler):
    start_urls = [
        'https://boingboing.net/tag/cannabis',
        'https://boingboing.net/tag/marijuana',
    ]
    source_id = 'boing-boing'

    config_selectors = {

        # Css selector on articles page (the page list many articles)
        'POST_URLS': '#container > article .entry-title > a::attr(href)',
        'NEXT_PAGE_URL': '#container > h2.entry-title a::attr(href)',  # default

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_AUTHOR': '.author a::text',
        'ARTICLE_CONTENT': '#story > *:not(div)',
    }


if __name__ == "__main__":
    crawler = CBoingBoingCrawler()
    crawler.run()