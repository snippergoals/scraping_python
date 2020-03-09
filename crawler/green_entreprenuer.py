# -*- coding: utf-8 -*-
""" Script to crawl Article from greenentrepreneur.com

green-entrepreneurs
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CGreenEntrepreneurCrawler(BaseCrawler):
    start_urls = [
        'https://www.greenentrepreneur.com/topic/news-and-trends',
    ]

    # source = 'Green Entrepreneur'
    source_id = 'green-entrepreneurs'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': 'a[href*=article]::attr(href)',
        'NEXT_PAGE_URL': '.active + li > a::attr(href)',  # default

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_AUTHOR': '[rel="author"] [itemprop=name]::text',
        'ARTICLE_CONTENT': '#articleAdd > *:not(div)',
    }


if __name__ == "__main__":
    crawler = CGreenEntrepreneurCrawler()
    crawler.run()