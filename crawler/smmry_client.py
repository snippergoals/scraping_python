import smmrpy
import requests
import logging


class SMMRYClient:
    SM_API_KEY_FREE = "51B2E354D1"
    SM_API_KEY_PAID = "54E2DA83D6"

    def __init__(self):
        self.SM_API_KEY = self.SM_API_KEY_FREE
        self.s = smmrpy.SMMRPY(self.SM_API_KEY)

    def summarization_by_content(self, content):
        logging.info('Using {} key'.format('free' if self.SM_API_KEY == self.SM_API_KEY_FREE else 'paid'))
        res = requests.post("https://api.smmry.com?SM_IGNORE_LENGTH=1&SM_API_KEY={}".format(self.SM_API_KEY), data={'sm_api_input': content})
        summarization = res.json().get('sm_api_content')
        if summarization is None:
            # logging.error("Exception in summarization by content: {}".format(res.text))
            if 'GO TO PARTNER PAGE FOR MORE' in res.text.upper():
                # logging.error("Need more smmry credits")
                self.SM_API_KEY = self.SM_API_KEY_PAID
                self.s = smmrpy.SMMRPY(self.SM_API_KEY)
                return self.summarization_by_content(content)
        return summarization
    
    def summarization_by_url(self, url):
        logging.info('Summarization by url: {}'.format(url))
        logging.info('Using {} key'.format('free' if self.SM_API_KEY == self.SM_API_KEY_FREE else 'paid'))
        smmry_article = s.get_smmry(url=url)
        return smmry_article.content
