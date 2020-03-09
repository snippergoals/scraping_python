# -*- coding: utf-8 -*-
""" Script to crawl Article from cbsnews.com

cbs-news
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CCBSNewsCrawler(BaseCrawler):
    start_urls = [
        'https://www.cbsnews.com/marijuana-nation/',

    ]

    # source = 'CBS News'
    source_id = 'cbs-news'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.listing-basic-lead .items > .item > a::attr(href)',
        'NEXT_PAGE_URL': 'a.load-more ::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '.content-article section',
    }


if __name__ == "__main__":
    crawler = CCBSNewsCrawler()
    crawler.run()