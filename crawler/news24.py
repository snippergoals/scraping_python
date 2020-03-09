# -*- coding: utf-8 -*-
""" Script to crawl Article from news24.com

news24
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CNews24Crawler(BaseCrawler):
    start_urls = [
        'https://www.news24.com/Tags/Topics/cannabis',
        'https://www.news24.com/Tags/Topics/marijuana',

    ]

    # source = 'News24'
    source_id = 'news24'

    config_selectors = {
         # Css selector on articles page (the page list many articles)
        'POST_URLS': '#divContainer > a::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '.article_content > p, #article-body > p',
        'ARTICLE_AUTHOR': '.author::text',
    }


if __name__ == "__main__":
    crawler = CNews24Crawler()
    crawler.run()