# -*- coding: utf-8 -*-
""" Script to crawl Article from newcannabisventures.com

new-cannabis-ventures
"""
try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler

class NewCannabisVenturesCrawler(BaseCrawler):
    start_urls = [
        'https://www.newcannabisventures.com',
        'https://www.newcannabisventures.com/category/breaking-news/',
        'https://www.newcannabisventures.com/category/exclusives/',
        'https://www.newcannabisventures.com/category/cannabis-thought-leader-news/',
        'https://www.newcannabisventures.com/category/cannabis-investor-news/',
        'https://www.newcannabisventures.com/category/cannabis-company-news/',
        'https://www.newcannabisventures.com/category/cannabis-products-and-services-news/',
        'https://www.newcannabisventures.com/category/publicly-traded-cannabis-stock-news/',
    ]

    # source = 'New Cannabis Ventures'
    source_id = 'new-cannabis-ventures'

    config_selectors = {
        'POST_URLS': '#main article .entry-title > a::attr(href)',
        'NEXT_PAGE_URL': '.pull-left.pagination-link > a::attr(href), .pagination-nav .current + a::attr(href)',
        'ARTICLE_CONTENT': '.entry-content > div.col-xs-12 > *:not(section):not(.article-tags)',
        'ARTICLE_PUBLISHED_AT': '[name="weibo:article:create_at"]::attr(content)',
        'ARTICLE_AUTHOR': '.post-author .category ::text',
    }


    # override parent's class method
    def extract_author(self, selector):
        v = super(NewCannabisVenturesCrawler, self).extract_author(selector)
        if v is not None:
            return v.split('by')[-1].strip()
        return None

if __name__ == "__main__":
    crawler = NewCannabisVenturesCrawler()
    crawler.run()
