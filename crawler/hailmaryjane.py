# -*- coding: utf-8 -*-
""" Script to crawl Article from www.hailmaryjane.com

hail-mary-jane
"""
try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler

class HailMaryJaneCrawler(BaseCrawler):
    start_urls = [
        'https://www.hailmaryjane.com/news/',
        'https://www.hailmaryjane.com/culture/',
        'https://www.hailmaryjane.com/guides/'
    ]

    # source = 'Hail Mary Jane'
    source_id = 'hail-mary-jane'

    config_selectors = {
        'POST_URLS': '#content_box article h3.title > a::attr(href)',
        'ARTICLE_CONTENT': '.thecontent > *:not(.kk-star-ratings)'
    }


if __name__ == "__main__":
    crawler = HailMaryJaneCrawler()
    crawler.run()