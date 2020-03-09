# -*- coding: utf-8 -*-
""" Script to crawl Article from news.weedmaps.com

weedmaps
"""
try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler

class WeedmapsCrawler(BaseCrawler):
    start_urls = [
        'https://news.weedmaps.com/culture-industry/',
        'https://news.weedmaps.com/law-politics/',
        'https://news.weedmaps.com/science-medicine/'
    ]

    # source = 'Weedmaps'
    source_id = 'weedmaps'

    config_selectors = {
        'POST_URLS': '#main .entry-title a::attr(href)',
        'ARTICLE_CONTENT': '#weedmaps-news-story > *:not(#post-lower-controls)',
        'ARTICLE_AUTHOR': '.wmnews-desktop .author-name ::text',
    }


if __name__ == "__main__":
    crawler = WeedmapsCrawler()
    crawler.run()