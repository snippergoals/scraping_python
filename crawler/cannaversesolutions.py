# -*- coding: utf-8 -*-
""" Script to crawl Article from cannaversesolutions.com

cannverse-solutions
"""
try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler

class CannaverseSolutionsCrawler(BaseCrawler):
    start_urls = [
        'https://cannaversesolutions.com/blog/'
    ]

    # source = 'Cannaverse Solutions'
    source_id = 'cannverse-solutions'

    config_selectors = {
        'POST_URLS': '.dfd-blog-title > a::attr(href)',
        'NEXT_PAGE_URL': '.prev-next-links .older::attr(href)',
        'ARTICLE_CONTENT': 'article > .entry-content > div:not(:first-child):not(:last-child)',
        'ARTICLE_AUTHOR': '.entry-meta .author ::text',
    }


if __name__ == "__main__":
    crawler = CannaverseSolutionsCrawler()
    crawler.run()