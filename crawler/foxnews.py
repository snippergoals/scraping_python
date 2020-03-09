# -*- coding: utf-8 -*-
""" Script to crawl Article from insider.foxnews.com

fox-news
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CFoxNewsCrawler(BaseCrawler):
    start_urls = [
        'https://insider.foxnews.com/tag/marijuana',

    ]

    # source = 'Fox News'
    source_id = 'fox-news'

    config_selectors = {
       # Css selector on articles page (the page list many articles)
        'POST_URLS': '.headline .title > a::attr(href)',
        'NEXT_PAGE_URL': '.next a::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '[property="content:encoded"] p::text',        
    }


if __name__ == "__main__":
    crawler = CFoxNewsCrawler()
    crawler.run()