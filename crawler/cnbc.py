# -*- coding: utf-8 -*-

""" Script to crawl Article from cnbc.com

cnbc
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CCNBCCrawler(BaseCrawler):
    start_urls = [
        'https://www.cnbc.com/marijuana/',
    ]

    # source = 'CNBC'
    source_id = 'cnbc'

    config_selectors = {
        'POST_URLS': '.stories_assetlist .headline > a::attr(href)',
        # 'ARTICLE_TITLE': '.title[itemprop="name"]',
        'ARTICLE_AUTHOR': '[itemprop="author"] [rel="author"] ::text',
        'ARTICLE_PUBLISHED_AT': '[itemprop="datePublished"]::attr(content)',
        'ARTICLE_CONTENT': '.group[itemprop="articleBody"], [itemprop="description"]',
        'NEXT_PAGE_URL': '.quickPagJump.rightPagCol > a::attr(href)',
    }


if __name__ == "__main__":
    crawler = CCNBCCrawler()
    crawler.run()