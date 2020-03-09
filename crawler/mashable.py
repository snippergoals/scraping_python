# -*- coding: utf-8 -*-
""" Script to crawl Article from mashable.com

mashable
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CMashableCrawler(BaseCrawler):
    start_urls = [
        'https://mashable.com/category/marijuana/',
        'https://mashable.com/category/marijuana-legalization/',
        'https://mashable.com/category/weed-in-america/',
        'https://mashable.com/category/medical-marijuana/',

    ]

    # source = 'Mashable'
    source_id = 'mashable'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.article-title > a::attr(href)',
        'NEXT_PAGE_URL': 'a[rel="next"]::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '.article-content.blueprint, .article-content',
        'ARTICLE_AUTHOR': '.byline  .author_name a::text, .article-info .byline::text',
        'ARTICLE_PUBLISHED_AT': '.byline time::attr(datetime), .article-info time::attr(datetime)',
    }


if __name__ == "__main__":
    crawler = CMashableCrawler()
    crawler.run()