# -*- coding: utf-8 -*-
""" Script to crawl Article from arstechnica.com

ars-technica
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CarsTechnicaCrawler(BaseCrawler):
    start_urls = [
        'https://arstechnica.com/tag/cannabis/',

    ]

    # source = 'ars Technica'
    source_id = 'ars-technica'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.listing  > ol > li.article > a::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '.article-content > p',
        'ARTICLE_AUTHOR': '.byline span[itemprop=name]::text',
        'ARTICLE_PUBLISHED_AT': '.post-meta .date::attr(datetime)',
    }


if __name__ == "__main__":
    crawler = CarsTechnicaCrawler()
    crawler.run()