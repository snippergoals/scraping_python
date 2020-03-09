# -*- coding: utf-8 -*-
""" Script to crawl Article from leafly.com

leafly
"""
try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler

class LeaflyCrawler(BaseCrawler):
    start_urls = [
        'https://www.leafly.com/news/category/cannabis-101',
        'https://www.leafly.com/news/category/growing',
        'https://www.leafly.com/news/category/strains-products',
        'https://www.leafly.com/news/category/politics',
        'https://www.leafly.com/news/category/health',
        'https://www.leafly.com/news/category/lifestyle',
        'https://www.leafly.com/news/category/science-tech',
        'https://www.leafly.com/news/category/industry',
        'https://www.leafly.com/news/category/canada'
    ]

    # source = 'Leafly'
    source_id = 'leafly'

    config_selectors = {
        'POST_URLS': '.post-body a.leafly-article::attr(href)',
        'ARTICLE_CONTENT': '.pos-center .uncont > .uncode_text_column',
        'ARTICLE_TITLE': '[propery="og:title"]::attr(content), [property="og:title"]::attr(content)',
        'ARTICLE_AUTHOR': '[name="sailthru.author"]::attr(content)',
        'ARTICLE_PUBLISHED_AT': '[propery="article:published_time"]::attr(content), [property="article:published_time"]::attr(content)',
        'ARTICLE_URL_TO_IMAGE': '[propery="og:image"]::attr(content), [property="og:image"]::attr(content)',   
    }


if __name__ == "__main__":
    crawler = LeaflyCrawler()
    crawler.run()