# -*- coding: utf-8 -*-
""" Script to crawl Article from abc.net.au

420-magazine
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CABCNewsAUCrawler(BaseCrawler):
    start_urls = [
        'https://www.abc.net.au/news/topic/cannabis',

    ]

    # source = 'ABC News AU'
    source_id = 'abc-news-au'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.article-index > li  h3 > a::attr(href)',
        'NEXT_PAGE_URL': '.next::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '.article.section > p:not([class])',
        'ARTICLE_AUTHOR': '.byline ::text',
    }


if __name__ == "__main__":
    crawler = CABCNewsAUCrawler()
    crawler.run()