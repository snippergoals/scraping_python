# -*- coding: utf-8 -*-
""" Script to crawl Article from marleynatural.com

marley-natural
"""
try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler

class MarleyNaturalCrawler(BaseCrawler):
    start_urls = [
        'https://www.marleynatural.com/blog/'
    ]

    # source = 'Marley Natural'
    source_id = 'marley-natural'

    config_selectors = {
        'POST_URLS': '.BlogList-item-title::attr(href)',
        'ARTICLE_CONTENT': '[data-layout-label="Post Body"]',
        'ARTICLE_AUTHOR': '.Blog-meta-item--author::text',
        'ARTICLE_PUBLISHED_AT': '.BlogItem-pagination-link-meta-item--date::attr(datetime)',
        'NEXT_PAGE_URL': '.BlogList-pagination a:last-child::attr(href)',

    }


if __name__ == "__main__":
    crawler = MarleyNaturalCrawler()
    crawler.run()