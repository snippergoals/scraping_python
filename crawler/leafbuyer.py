# -*- coding: utf-8 -*-
""" Script to crawl Article from leafbuyer.com

leafbuyer
"""
try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler

class LeafbuyerCrawler(BaseCrawler):
    start_urls = [
        'https://www.leafbuyer.com/blog?s=',
        'https://www.leafbuyer.com/blog/category/cannabis-news',
        'https://www.leafbuyer.com/blog/category/marijuana-101/',
        'https://www.leafbuyer.com/blog/category/cannabis-culture',
    ]

    # source = 'Leafbuyer'
    source_id = 'leafbuyer'

    config_selectors = {
        'POST_URLS': '.td-ss-main-content .entry-title > a::attr(href)',
        'NEXT_PAGE_URL': '.page-nav .current + a.page::attr(href)',
        'ARTICLE_CONTENT': '.td-post-content > *:not(.sfsi_Sicons)',
        'ARTICLE_TITLE': 'h1.entry-title ::text',
        'ARTICLE_PUBLISHED_AT': '[itemprop="datePublished"]::attr(content)',
        'ARTICLE_URL_TO_IMAGE': '[itemprop="image"] [itemprop=url]::attr(content)',
    }


if __name__ == "__main__":
    crawler = LeafbuyerCrawler()
    crawler.run()