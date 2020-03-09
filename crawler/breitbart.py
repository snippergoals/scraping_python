# -*- coding: utf-8 -*-
""" Script to crawl Article from breitbart.com

breitbart
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CBreitbartCrawler(BaseCrawler):
    start_urls = [
        'https://www.breitbart.com/tag/medical-marijuana/',
        'https://www.breitbart.com/tag/cannabis/',

    ]

    # source = 'Breitbart'
    source_id = 'breitbart'

    config_selectors = {
         # Css selector on articles page (the page list many articles)
        'POST_URLS': 'article h2 > a::attr(href)',
        'NEXT_PAGE_URL': '.pagination [rel=next] ::attr(href)',
        
        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '.entry-content',
        'ARTICLE_AUTHOR': 'address[data-auri*=author] ::text',
    }


if __name__ == "__main__":
    crawler = CBreitbartCrawler()
    crawler.run()