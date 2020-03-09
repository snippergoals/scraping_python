# -*- coding: utf-8 -*-
""" Script to crawl Article from thehill.com

the-hill
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CTheHillCrawler(BaseCrawler):
    start_urls = [
        'https://thehill.com/social-tags/marijuana',

    ]

    # source = 'The Hill'
    source_id = 'the-hill'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.node__title > a::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '[property="content:encoded"]',
        'ARTICLE_AUTHOR': '.submitted-by a::text, .submitted-by::text',
    }


if __name__ == "__main__":
    crawler = CTheHillCrawler()
    crawler.run()