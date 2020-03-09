# -*- coding: utf-8 -*-
""" Script to crawl Article from cannabisculture.com

cannabis-culture
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CCannabisCultureCrawler(BaseCrawler):
    start_urls = [
        'https://www.cannabisculture.com',
        'https://www.cannabisculture.com/activism/',
        'https://www.cannabisculture.com/medical/',
        'https://www.cannabisculture.com/arts/',
        'https://www.cannabisculture.com/hemp/',
        'https://www.cannabisculture.com/blogs/',

    ]

    # source = 'Cannabis Culture'
    source_id = 'cannabis-culture'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': 'a[href*=content]::attr(href)',
        # 'NEXT_PAGE_URL': '.table-cell .th-btn::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '[itemprop="articleBody"]',
        'ARTICLE_AUTHOR': '.posted-by ::text',
        # 'ARTICLE_PUBLISHED_AT': '[name="published_at"]::attr(content)',
    }


if __name__ == "__main__":
    crawler = CCannabisCultureCrawler()
    crawler.run()