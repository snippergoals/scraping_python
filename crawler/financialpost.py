# -*- coding: utf-8 -*-
""" Script to crawl Article from business.financialpost.com

financial-post
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CFinancialPostCrawler(BaseCrawler):
    start_urls = [
        'https://business.financialpost.com/category/cannabis',
        'https://business.financialpost.com/tag/marijuana',

    ]

    # source = 'Financial Post'
    source_id = 'financial-post'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.entry-title > a::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '[itemprop="articleBody"]',
    }


if __name__ == "__main__":
    crawler = CFinancialPostCrawler()
    crawler.run()