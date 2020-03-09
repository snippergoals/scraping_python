# -*- coding: utf-8 -*-

""" Script to crawl Article from marketwatch.com

cannabis-watch
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CCannabisWatchCrawler(BaseCrawler):
    start_urls = [
        'https://www.marketwatch.com/column/cannabis-watch',
    ]

    # source = 'Cannabis Watch'
    source_id = 'cannabis-watch'

    config_selectors = {
        'POST_URLS' : '.region--primary .article__headline > a::attr(href)',
        'ARTICLE_TITLE': '#article-headline::text',
        'ARTICLE_AUTHOR': '#author-bylines [rel="author"]::text',
        'ARTICLE_PUBLISHED_AT': '#published-timestamp span::text',
        'ARTICLE_URL_TO_IMAGE': '.article-image::attr(src)',
        'ARTICLE_CONTENT': '#article-body > p ::text'
    }


if __name__ == "__main__":
    crawler = CCannabisWatchCrawler()
    crawler.run()