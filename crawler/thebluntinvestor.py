# -*- coding: utf-8 -*-
""" Script to crawl Article from thebluntinvestor.com

the-blunt-investor
"""
try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler

class TheBluntInvestorCrawler(BaseCrawler):
    start_urls = [
        'https://thebluntinvestor.com/news/',
        'https://thebluntinvestor.com/trending/',
    ]

    # source = 'The Blunt Investor'
    source_id = 'the-blunt-investor'

    config_selectors = {
        'POST_URLS': '#primary article .entry-header > h3 > a::attr(href)',
        'ARTICLE_CONTENT': '[itemprop="articleBody"]',
        'ARTICLE_AUTHOR': '[rel="author"] [itemprop="name"]::text',

    }


if __name__ == "__main__":
    crawler = TheBluntInvestorCrawler()
    crawler.run()