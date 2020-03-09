# -*- coding: utf-8 -*-
""" Script to crawl Article from abcnews.com

abc-news
"""
try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler


class CABCNewsCrawler(BaseCrawler):
    start_urls = [
        'https://abcnews.go.com/alerts/marijuana',
    ]

    # source = 'ABC News'
    source_id = 'abc-news'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': 'h2[class*=TopicsList__topicsListItemHeader] > a::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '.article-copy',
        'ARTICLE_AUTHOR': 'div.author::text',
        'ARTICLE_PUBLISHED_AT': 'span.timestamp::text',
    }

    #override method
    def extract_published_at(self, selector):
        return selector.xpath('//script[contains(text(), "datePublished")]/text()').extract_first('').split('"datePublished":"', 1)[-1].split('"', 1)[0].strip()

if __name__ == "__main__":
    crawler = CABCNewsCrawler()
    crawler.run()