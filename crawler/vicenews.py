# -*- coding: utf-8 -*-
""" Script to crawl Article from news.vice.com

vice-news
"""
try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CViceNewsCrawler(BaseCrawler):
    start_urls = [
        'https://www.vice.com/en_us/topic/marijuana',
        'https://www.vice.com/en_us/topic/cannabis',
    ]

    # source = 'Vice News'
    source_id = 'vice-news'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': 'a[href*=article]::attr(href)',
        # 'NEXT_PAGE_URL': '.pager-next > a::attr(href)',  # default

        # Css selector on article's detail page (the page display full content of article)
        # 'ARTICLE_PUBLISHED_AT': '.published',
        'ARTICLE_AUTHOR': '[property="article:author"]::attr(content)',
        'ARTICLE_CONTENT': 'div.post-content > p, .article__body > p',

    }


if __name__ == "__main__":
    crawler = CViceNewsCrawler()
    crawler.run()