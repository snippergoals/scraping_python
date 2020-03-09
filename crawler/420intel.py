# -*- coding: utf-8 -*-
""" Script to crawl Article from 420intel.com

420-intel
"""
try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class C420IntelCrawler(BaseCrawler):
    start_urls = [
        'https://420intel.com/articles/medical-cannabis-news',
        'https://420intel.com/articles/recreational-marijuana-news',
        'https://420intel.com/articles/marijuana-business-news',
        'https://420intel.com/articles/cannabis-technology-news',
        'https://420intel.com/articles/marijuana-politics',
    ]

    # source = '420 Intel'
    source_id = '420-intel'

    config_selectors = {
        'POST_URLS': '.node-article .node-title > a::attr(href)',
        'ARTICLE_CONTENT': '.field-name-body',
        'ARTICLE_AUTHOR': '[name="dcterms.creator"]::attr(content)',
        'NEXT_PAGE_URL': '.pager-next > a::attr(href)',
    }


if __name__ == "__main__":
    crawler = C420IntelCrawler()
    crawler.run()