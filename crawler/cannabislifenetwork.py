# -*- coding: utf-8 -*-
""" Script to crawl Article from cannabislifenetwork.com

cannabis-life-network
"""
try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler

class CannabisLifeNetworkCrawler(BaseCrawler):
    start_urls = [
        'https://cannabislifenetwork.com/category/news/',
        'https://cannabislifenetwork.com/category/news/business/',
        'https://cannabislifenetwork.com/category/news/culture/',
        'https://cannabislifenetwork.com/category/news/health/',
        'https://cannabislifenetwork.com/category/news/law/',
        'https://cannabislifenetwork.com/category/news/politics/',
        'https://cannabislifenetwork.com/category/news/science/',
        'https://cannabislifenetwork.com/category/news/technology/',
    ]

    # source = 'Cannabis Life Network'
    source_id = 'cannabis-life-network'

    config_selectors = {
        'POST_URLS': '#main article h2.cb-post-title > a::attr(href)',
        'ARTICLE_CONTENT': '.cb-entry-content > *:not(.addtoany_share_save_container)',
        'ARTICLE_AUTHOR': '[rel=author]::text',
    }


if __name__ == "__main__":
    crawler = CannabisLifeNetworkCrawler()
    crawler.run()