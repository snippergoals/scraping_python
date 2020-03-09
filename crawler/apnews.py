# -*- coding: utf-8 -*-
""" Script to crawl Article from apnews.com

ap-news
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CAPNewsCrawler(BaseCrawler):
    start_urls = [
        'https://www.apnews.com/Medicalmarijuana',
        'https://www.apnews.com/Cannabis',
        'https://www.apnews.com/CaliforniaMarijuana',

    ]

    # source = 'AP News'
    source_id = 'ap-news'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.FeedCard .headline::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '.Article',
        'ARTICLE_AUTHOR': '.byline ::text',
    }


if __name__ == "__main__":
    crawler = CAPNewsCrawler()
    crawler.run()