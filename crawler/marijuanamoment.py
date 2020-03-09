# -*- coding: utf-8 -*-
""" Script to crawl Article from marijuanamoment.net

marijuana-moment
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CMarijuanMomentCrawler(BaseCrawler):
    start_urls = [
        'https://www.marijuanamoment.net/category/politics/',
        'https://www.marijuanamoment.net/category/science-and-health/',
        'https://www.marijuanamoment.net/category/culture/',
        'https://www.marijuanamoment.net/category/business/',
        'https://www.marijuanamoment.net/category/video/',

    ]

    # source = 'Marijuana Moment'
    source_id = 'marijuana-moment'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': '[rel="bookmark"]::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '#mvp-content-main > p',
        'ARTICLE_AUTHOR': '#mvp-post-head .author-name  > a::text',
    }


if __name__ == "__main__":
    crawler = CMarijuanMomentCrawler()
    crawler.run()