# -*- coding: utf-8 -*-
""" Script to crawl Article from 420magazine.com

420-magazine
"""
try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler

class C420MagazineCrawler(BaseCrawler):
    start_urls = [
        'https://www.420magazine.com/articles/420-news/',
        'https://www.420magazine.com/articles/420-news/international-cannabis-news/',
        'https://www.420magazine.com/articles/420-news/medical-marijuana-news/', 
        'https://www.420magazine.com/articles/hemp/industrial-hemp-news/'
    ]

    # source = '420 Magazine'
    source_id = '420-magazine'

    config_selectors = {
        'POST_URLS': '.td-ss-main-content .item-details > h3 > a::attr(href)',
        'ARTICLE_CONTENT': '.td-post-content',
        'ARTICLE_AUTHOR': '.td-post-author-name > a ::text',
        'ARTICLE_TITLE': '.td-post-title > h1.entry-title::text',
        'ARTICLE_PUBLISHED_AT': '[itemprop="datePublished"]::attr(content)',
    }


if __name__ == "__main__":
    crawler = C420MagazineCrawler()
    crawler.run()