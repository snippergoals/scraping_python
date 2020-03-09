# -*- coding: utf-8 -*-
""" Script to crawl Article from thecannabist.co

the-cannabist
"""
try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler

class TheCannabistCrawler(BaseCrawler):
    start_urls = [
        'https://www.thecannabist.co/category/colorado-news/',
        'https://www.thecannabist.co/category/news/us-news/',
        'https://www.thecannabist.co/category/news/world-news/',
        'https://www.thecannabist.co/category/business/ ',
        'https://www.thecannabist.co/category/crime/ ',
    ]

    # source = 'The Cannabist'
    source_id = 'the-cannabist'

    config_selectors = {
        'POST_URLS': '.multi-column > li > article h2 > a::attr(href)',
        'ARTICLE_CONTENT': '#content .entry-content',
        'ARTICLE_AUTHOR': '[rel="author"]::text, .byline > strong::text, .byline > em::text',

    }


if __name__ == "__main__":
    crawler = TheCannabistCrawler()
    crawler.run()