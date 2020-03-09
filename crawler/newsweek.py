# -*- coding: utf-8 -*-
""" Script to crawl Article from newsweek.com

newsweek
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CNewsweekCrawler(BaseCrawler):
    start_urls = [
        'https://www.newsweek.com/topic/marijuana',
        'https://www.newsweek.com/topic/medical-marijuana',
        'https://www.newsweek.com/topic/marijuana-legalization',

    ]

    # source = 'Newsweek'
    source_id = 'newsweek'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': 'article h3 >a::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '.article-body',
        'ARTICLE_AUTHOR': '.byline > .author ::text',
    }


if __name__ == "__main__":
    crawler = CNewsweekCrawler()
    crawler.run()