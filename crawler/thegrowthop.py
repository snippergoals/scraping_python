# -*- coding: utf-8 -*-
""" Script to crawl Article from thegrowthop.com

the-growth-op
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CTheGrowthOPCrawler(BaseCrawler):
    start_urls = [
        'https://www.thegrowthop.com/category/cannabis-business',
        'https://www.thegrowthop.com/category/cannabis-health',
        'https://www.thegrowthop.com/category/cannabis-news',
        'https://www.thegrowthop.com/category/cannabis-culture',

    ]

    # source = 'The Growth OP'
    source_id = 'the-growth-op'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.article-title > a::attr(href)',
        'NEXT_PAGE_URL': '.table-cell .th-btn::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '[itemprop="articleBody"]',
        'ARTICLE_AUTHOR': '.post-author ::text',
    }


if __name__ == "__main__":
    crawler = CTheGrowthOPCrawler()
    crawler.run()