# -*- coding: utf-8 -*-
""" Script to crawl Article from cannalawblog.com

canna-law-blog
"""
try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler

class CannaLawBlogCrawler(BaseCrawler):
    start_urls = [
        'https://www.cannalawblog.com'
    ]

    # source = 'Canna Law Blog'
    source_id = 'canna-law-blog'

    config_selectors = {
        'POST_URLS': 'article h1 > a::attr(href)',
        'ARTICLE_CONTENT': '.lxb_af-post_content',
        'ARTICLE_AUTHOR': 'header[role="presentation"] a.lxb_af-template_tags-get_author::text',
    }


if __name__ == "__main__":
    crawler = CannaLawBlogCrawler()
    crawler.run()