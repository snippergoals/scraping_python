# -*- coding: utf-8 -*-
""" Script to crawl Article from fastcompany.com

fast-company
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CFastCompanyCrawler(BaseCrawler):
    start_urls = [
        'https://www.fastcompany.com/section/marijuana',
        'https://www.fastcompany.com/section/cannabis',
    ]

    # source = 'Fast Company'
    source_id = 'fast-company'

    config_selectors = {

        # Css selector on articles page (the page list many articles)
        'POST_URLS': 'div.all-feed__section  article > a::attr(href)',
        'NEXT_PAGE_URL': '.all-feed__button > a::attr(href)',  # default

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_AUTHOR': '[property="author"]::attr(content)',
        'ARTICLE_CONTENT': 'article.post__article',
    }


if __name__ == "__main__":
    crawler = CFastCompanyCrawler()
    crawler.run()