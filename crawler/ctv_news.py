# -*- coding: utf-8 -*-
""" Script to crawl Article from ctvnews.ca

ctv-news
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CCTVNewsCrawler(BaseCrawler):
    start_urls = [
        'https://www.ctvnews.ca/canada/ctv-news-marijuana-legalization-in-canada',
    ]

    # source = 'CTV News'
    source_id = 'ctv-news'

    config_selectors = {

        # Css selector on articles page (the page list many articles)
        'POST_URLS': 'a[href*="-1."][href*="ctvnews.ca"]::attr(href)',
        'NEXT_PAGE_URL': 'h3 > a::attr(href)',  # default

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '.articleBody',
    }


if __name__ == "__main__":
    crawler = CCTVNewsCrawler()
    crawler.run()