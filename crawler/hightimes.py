# -*- coding: utf-8 -*-
""" Script to crawl Article from hightimes.com

high-times
"""
try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler

class HighTimesCrawler(BaseCrawler):
    start_urls = [
        'https://hightimes.com/news/legalization/',
        'https://hightimes.com/news/',
        'https://hightimes.com/health/medical-marijuana/ ',
        'https://hightimes.com/grow/',
        'https://hightimes.com/health/',
        'https://hightimes.com/culture/',
        'https://hightimes.com/products/',
        'https://hightimes.com/activism/',
    ]

    # source = 'High Times'
    source_id = 'high-times'

    config_selectors = {
        'POST_URLS': '.mvp-blog-story-list > li > a::attr(href)',
        'ARTICLE_CONTENT': '.theiaPostSlider_slides',
        'ARTICLE_AUTHOR': '[rel="author"] ::text',

    }


if __name__ == "__main__":
    crawler = HighTimesCrawler()
    crawler.run()