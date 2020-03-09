# -*- coding: utf-8 -*-
""" Script to crawl Article from hempindustrydaily.com

hemp-industry-daily
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CHempIndustryDailyCrawler(BaseCrawler):
    start_urls = [
        'https://hempindustrydaily.com',
        'https://hempindustrydaily.com/fiber-and-grain/',
        'https://hempindustrydaily.com/retail/',
        'https://hempindustrydaily.com/legal-news/',
        'https://hempindustrydaily.com/cultivation-processing-extraction/',
        'https://hempindustrydaily.com/finance-investing-and-banking/',
        'https://hempindustrydaily.com/ancillary-hemp-companies/',

    ]

    # source = 'Hemp Industry Daily'
    source_id = 'hemp-industry-daily'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': 'article h2 > a::attr(href)',
        # 'NEXT_PAGE_URL': '.table-cell .th-btn::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '.entry-content > p',
        'ARTICLE_URL_TO_IMAGE': '[property="og:image"]::attr(content)',
    }


if __name__ == "__main__":
    crawler = CHempIndustryDailyCrawler()
    crawler.run()