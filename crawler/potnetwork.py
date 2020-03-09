# -*- coding: utf-8 -*-
""" Script to crawl Article from potnetwork.com

pot-network
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CPotNetworkCrawler(BaseCrawler):
    start_urls = [
        'https://www.potnetwork.com/finance-investing',
        'https://www.potnetwork.com/marijuana-healthcare',
        'https://www.potnetwork.com/media',
        'https://www.potnetwork.com/business-services',
        'https://www.potnetwork.com/technology',
        'https://www.potnetwork.com/cultivation',
        'https://www.potnetwork.com/manufacturing-distribution',
        'https://www.potnetwork.com/retail',

    ]

    # source = 'Pot Network'
    source_id = 'pot-network'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.node-title > a::attr(href)',
        'NEXT_PAGE_URL': '.pager__item--next > a::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '#article > div.field-node--body',
        'ARTICLE_AUTHOR': '.article-author-name ::text',
        'ARTICLE_PUBLISHED_AT': '.column-info-meta div:nth-child(1)::text',    
    }


if __name__ == "__main__":
    crawler = CPotNetworkCrawler()
    crawler.run()