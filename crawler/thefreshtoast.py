# -*- coding: utf-8 -*-
""" Script to crawl Article from thefreshtoast.com

the-fresh-toast
"""
try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler

class TheFreshToastCrawler(BaseCrawler):
    start_urls = [
        'https://thefreshtoast.com/category/cannabis/'
    ]

    # source = 'The Fresh Toast'
    source_id = 'the-fresh-toast'

    config_selectors = {
        'POST_URLS': '.card--horizontal__right > a::attr(href), h3.entry-title> a::attr(href)',
        'ARTICLE_CONTENT': '.entry__content > *:not(.gf_browser_unknown), .tdb-block-inner.td-fix-index > p',
        'ARTICLE_AUTHOR': '.entry__author [rel=author]::text',
    }


if __name__ == "__main__":
    crawler = TheFreshToastCrawler()
    crawler.run()