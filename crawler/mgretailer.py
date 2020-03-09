# -*- coding: utf-8 -*-
""" Script to crawl Article from mgretailer.com

mg-retailer
"""
try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler

class MGMagazineCrawler(BaseCrawler):
    start_urls = [
        'https://mgretailer.com/cannabis-news/'
    ]

    # source = 'MG Magazine'
    source_id = 'mg-retailer'

    config_selectors = {
        'POST_URLS': '.td-ss-main-content .entry-title > a::attr(href)',
        'ARTICLE_CONTENT': '.theiaPostSlider_slides > div > *:not(.robots-nocontent)',
        'ARTICLE_AUTHOR': '.td-post-author-name > a::text',
    }


if __name__ == "__main__":
    crawler = MGMagazineCrawler()
    crawler.run()