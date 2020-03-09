# -*- coding: utf-8 -*-
""" Script to crawl Article from thejointblog.com

the-joint-blog
"""
try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler

class TheJointBlogCrawler(BaseCrawler):
    start_urls = [
        'https://thejointblog.com/category/news/'
    ]

    # source = 'The Joint Blog'
    source_id = 'the-joint-blog'

    config_selectors = {
        'POST_URLS': '.entry-title > a::attr(href)',
        'ARTICLE_CONTENT': '.entry-content > *:not(.first-child):not(.last-child)',
        'ARTICLE_AUTHOR': '.author [rel=author]::text',
        'ARTICLE_TITLE': 'h1.post-title::text',
    }

    # override parent's class method
    def extract_title(self, selector):
        css = self.config_selectors.get('ARTICLE_TITLE')
        return selector.css(css).extract_first('').strip()

if __name__ == "__main__":
    crawler = TheJointBlogCrawler()
    crawler.run()