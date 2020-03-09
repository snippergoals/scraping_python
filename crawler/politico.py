# -*- coding: utf-8 -*-
""" Script to crawl Article from politico.com

politico
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CPoliticoCrawler(BaseCrawler):
    start_urls = [
        'https://www.politico.com/news/marijuana',

    ]

    # source = 'Politico'
    source_id = 'politico'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.story-frag-list article.format-m h3 > a[href*=story]::attr(href)',
        'NEXT_PAGE_URL': '.pagination .current + li > a::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '.story-text  > p',
        'ARTICLE_PUBLISHED_AT': '[itemprop="datePublished"]::attr(datetime)',
    }


if __name__ == "__main__":
    crawler = CPoliticoCrawler()
    crawler.run()