# -*- coding: utf-8 -*-
""" Script to crawl Article from usnews.com

us-news
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CUSNewsCrawler(BaseCrawler):
    start_urls = [
        'https://www.usnews.com/topics/subjects/marijuana',
    ]

    # source = 'US News'
    source_id = 'us-news'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': 'h3 > a::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': 'div[class*=ArticleGroupings__BodyCell]',
    }


if __name__ == "__main__":
    crawler = CUSNewsCrawler()
    crawler.run()