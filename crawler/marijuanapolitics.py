# -*- coding: utf-8 -*-
""" Script to crawl Article from marijuanapolitics.com

marijuana-politics
"""
try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler

class MarijuanaPoliticsCrawler(BaseCrawler):
    start_urls = [
        'http://marijuanapolitics.com',
        'http://marijuanapolitics.com/politics/',
        'http://marijuanapolitics.com/business/',
        'http://marijuanapolitics.com/culture/',
        'http://marijuanapolitics.com/entertainment/',
        'http://marijuanapolitics.com/science/',
    ]

    # source = 'Marijuana Politics'
    source_id = 'marijuana-politics'

    config_selectors = {
        'POST_URLS': '.post > a::attr(href)',
        'ARTICLE_CONTENT': '.entry-content > *:not(#author-bio-box)',
        'ARTICLE_AUTHOR': '.author [rel=author]::text'
    }


if __name__ == "__main__":
    crawler = MarijuanaPoliticsCrawler()
    crawler.run()