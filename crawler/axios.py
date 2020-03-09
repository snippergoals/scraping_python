# -*- coding: utf-8 -*-
""" Script to crawl Article from axios.com

axios
"""
import re
try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CAxiosCrawler(BaseCrawler):
    start_urls = [
        'https://www.axios.com/tag/marijuana/',
        'https://www.axios.com/tag/legalized-marijuana/',
        'https://www.axios.com/tag/medical-marijuana/',

    ]

    # source = 'Axios'
    source_id = 'axios'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        # 'POST_URLS': 'article > a::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '[itemprop="articleBody"] > div:not(.qa-keep-reading)',
        'ARTICLE_AUTHOR': '[itemprop="author"] ::text',
        'ARTICLE_PUBLISHED_AT': '[itemprop="datePublished"]::attr(datetime)',
    }


    # override method
    def extract_post_urls(self, selector, html):
        return re.findall(r'"seo_headline":"","permalink":"(.*?)"', html)

if __name__ == "__main__":
    crawler = CAxiosCrawler()
    crawler.run()