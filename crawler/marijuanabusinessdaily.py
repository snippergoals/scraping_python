# -*- coding: utf-8 -*-
""" Script to crawl Article from mjbizdaily.com

marijuana-business-daily
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CMJBusinessDailyCrawler(BaseCrawler):
    start_urls = [
        'https://mjbizdaily.com',
        'https://mjbizdaily.com/category/international-marijuana-business-news/',
        'https://mjbizdaily.com/canada/',
        'https://mjbizdaily.com/category/canada-medical-marijuana-news/',
        'https://mjbizdaily.com/category/vendor-supplier-news/',
        'https://mjbizdaily.com/category/charts/',
        'https://mjbizdaily.com/category/dispensary-news/',
        'https://mjbizdaily.com/category/recreational/',
        'https://mjbizdaily.com/category/legal-news/',
        'https://mjbizdaily.com/category/financial-news/',
        'https://mjbizdaily.com/category/cultivation/',
        'https://mjbizdaily.com/category/edibles-infused-products/',
        'https://mjbizdaily.com/category/stocks/',

    ]

    # source = 'MJ Business Daily'
    source_id = 'marijuana-business-daily'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.entry-title > a::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '.entry-content',
    }


if __name__ == "__main__":
    crawler = CMJBusinessDailyCrawler()
    crawler.run()