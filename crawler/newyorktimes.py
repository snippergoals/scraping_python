# -*- coding: utf-8 -*-
""" Script to crawl Article from nytimes.com

new-york-times
"""

try:
    from crawler import BaseCrawler
except:
    from __init__ import BaseCrawler
import logging
import json

class CNewYorkTimesCrawler(BaseCrawler):
    start_urls = [
        'https://www.nytimes.com/svc/collections/v1/publish/topics.nytimes.com/topic/subject/marijuana-and-medical-marijuana?q=&sort=newest&page=0&dom=www.nytimes.com&dedupe_hl=y'
    ]

    # source = 'The New York Times'
    source_id = 'new-york-times'

    config_selectors = {
        # Css selector on articles page (the page list many articles)
        # Css selector on article's detail page (the page display full content of article)
        'ARTICLE_CONTENT': '[name=articleBody]',
        'ARTICLE_AUTHOR': '[itemprop="author creator"] ::text, #byline span:not([class])::text',
        'ARTICLE_PUBLISHED_AT': 'time[datetime]::attr(datetime), [name="pdate"]::attr(content)',
    }

    # override method
    def parse_posts(self, response, url):
        logging.info('Parsing posts page: ' + url)
        post_urls = []
        jo = json.loads(response.text)
        for item in jo.get('members', {}).get('items', []):
            post_urls.append(item.get('url'))

        page = jo.get('members', {}).get('page', 0)
        total_pages = jo.get('members', {}).get('total_pages', 0)
        if page < total_pages:
            next_page_url = 'https://www.nytimes.com/svc/collections/v1/publish/topics.nytimes.com/topic/subject/marijuana-and-medical-marijuana?q=&sort=newest&page={0}&dom=www.nytimes.com&dedupe_hl=y'.format(page+1)
        else:
            next_page_url = None

        return post_urls, next_page_url

if __name__ == "__main__":
    crawler = CNewYorkTimesCrawler()
    crawler.run()