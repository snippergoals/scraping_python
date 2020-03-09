# -*- coding: utf-8 -*-
""" Script to crawl Article from grizzle.com

grizzle
"""
try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler

class GrizzleCrawler(BaseCrawler):
    start_urls = [
        'https://grizzle.com/marijuana/',
        'https://grizzle.com/marijuana/marijuana-investing/',
        'https://grizzle.com/marijuana/marijuana-politics/',
    ]

    # source = 'Grizzle'
    source_id = 'grizzle'

    config_selectors = {
        'POST_URLS': '#cb-content article > div > a::attr(href)',
        'ARTICLE_CONTENT': '[itemprop="articleBody"] .cb-itemprop'
    }


if __name__ == "__main__":
    crawler = GrizzleCrawler()
    crawler.run()