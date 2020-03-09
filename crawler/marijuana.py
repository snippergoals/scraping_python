# -*- coding: utf-8 -*-
""" Script to crawl Article from marijuana.com

marijuana
"""
try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler

class MarijuanaCrawler(BaseCrawler):
    start_urls = [
        'https://www.marijuana.com/news/category/law-politics/',
        'https://www.marijuana.com/news/category/health-medicine/',
        'https://www.marijuana.com/news/category/entertainment/',
        'https://www.marijuana.com/news/category/reviews/',
        'https://www.marijuana.com/news/category/opinion/'
    ]

    # source = 'Marijuana.com'
    source_id = 'marijuana'

    config_selectors = {
        'POST_URLS': '.row.listing article > h2 > a::attr(href)',
        'ARTICLE_CONTENT': '[itemprop="articleBody"] > p',
        'ARTICLE_AUTHOR': '.posted-by > span ::text',

    }


if __name__ == "__main__":
    crawler = MarijuanaCrawler()
    crawler.run()