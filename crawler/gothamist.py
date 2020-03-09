# -*- coding: utf-8 -*-
""" Script to crawl Article from gothamist.com

gothamist
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CGothamistCrawler(BaseCrawler):
    start_urls = [
        'http://gothamist.com/tags/marijuana',
    ]

    # source = 'Gothamist'
    source_id = 'gothamist'

    config_selectors = {

        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.entry-title a::attr(href)',
        'NEXT_PAGE_URL': 'div.next a::attr(href)',  # default

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_PUBLISHED_AT': '.published::text',
        'ARTICLE_AUTHOR': '.author a::text',
        'ARTICLE_CONTENT': '.entry-body > p',
    }

if __name__ == "__main__":
    crawler = CGothamistCrawler()
    crawler.run()