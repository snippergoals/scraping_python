# -*- coding: utf-8 -*-
""" Script to crawl Article from huffpost.com

huffington-post
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler
import logging
import traceback

class CHuffingtonPostCrawler(BaseCrawler):
    start_urls = [
        'https://www.huffpost.com/impact/topic/marijuana',
        'https://www.huffpost.com/topic/cannabis',
        'https://www.huffpost.com/topic/legalizing-marijuana',

    ]

    # source = 'The Huffington Post'
    source_id = 'huffington-post'

    def __init__(self):
        super().__init__()

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        'POST_URLS': '.a-page__content div.card .card__headline > a::attr(href), .card__headlines > a::attr(href)',
        'NEXT_PAGE_URL': '.table-cell .th-btn::attr(href)',

        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '.entry__body .entry__text .content-list-component',
    }

    def parse_posts(self, response, url):
        post_urls, next_page_url = super().parse_posts(response, url)
        if len(post_urls) > 0 :
            return post_urls, next_page_url
        
        try:
            jO = response.json()
            for card in jO['cards']:
                for headline in card['headlines']:
                    post_urls.append('https://www.huffpost.com{0}'.format(headline['url']))
            if jO['meta']['nextPage']:
                page = url.split('page=')[-1].split('&')[0]
                next_page_url = 'https://www.huffpost.com/life/api/topic/medical-marijuana/cards?page={0}'.format(int(page)+1)
            else:
                next_page_url = None
        except Exception as ex:
            logging.error("Exception in parse_posts: {0}".format(url))

        return post_urls, next_page_url

if __name__ == "__main__":
    crawler = CHuffingtonPostCrawler()
    crawler.run()