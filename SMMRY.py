import time
import asyncio
import smmrpy
from pymongo import MongoClient
import requests
import logging
import traceback
from urllib.parse import urlencode, quote_plus
import json


async def main():
    
    SM_API_KEY = "54E2DA83D6"
    s = smmrpy.SMMRPY(SM_API_KEY)
    client = MongoClient('localhost', 27017)
    db = client.NewsAPI
    collection = db.Articles

    for i in range(0, 100000):
        article = collection.find_one({'summarization': None})
        content = None
        if article is None:
            break
        summarization = ""
        if article.get('content') is not None and article.get('content').endswith(' chars]') == False:
            try:
                logging.info('Summarization by content: {0}'.format(article.get('url')))
                res = requests.post("https://api.smmry.com?SM_API_KEY={0}".format(SM_API_KEY), data={'sm_api_input': article.get('content')})
                summarization = res.json().get('sm_api_content')
                if summarization is None:
                    logging.error("Exception in summarization by content: {0}".format(res.text))
                    if 'GO TO PARTNER PAGE FOR MORE' in res.text.upper():
                        logging.error("Need more smmry credits")
                        break

            except Exception as ex:
                logging.error("Exception in summarization by content: {0}".format(article.get('content')))
                traceback.print_exc()
                summarization = ""
                if 'GO TO PARTNER PAGE FOR MORE' in str(ex).upper():
                    logging.error("Need more smmry credits")
                    break
        
        if (summarization is None or summarization == "") and article.get('url') is not None:
            try:
                logging.info('Summarization by url: {0}'.format(article.get('url')))
                smmry_article = await s.get_smmry(url=article.get('url'))
                summarization = smmry_article.content
            except Exception as ex:
                logging.error("Exception in summarization by url: {0}".format(article.get('url')))
                traceback.print_exc()
                summarization = ""
                if 'GO TO PARTNER PAGE FOR MORE' in str(ex).upper():
                    logging.error("Need more smmry credits")
                    break
        
        if (summarization is None or summarization == "") and article.get('url') is not None:
            # call diffbot to extract content then call smmry by content
            try:
                payload = {'callback': 'jQuery111105923303317213029_1548924875038',
                            'token':'testdriverehjenztgeil',
                            'url': article.get('url'),
                            'format':'jsonp',
                            '_': int(time.time())
                            }
                diffbot_url = "https://labs.diffbot.com/testdrive/article?{0}".format(urlencode(payload, quote_via=quote_plus))
                res = requests.get(diffbot_url)
                diff_article = json.loads(res.text.split('(', 1)[-1].rsplit(')')[0].strip())
                content = diff_article.get('objects', [{}])[0].get('text')
                if content is not None:
                    try:
                        logging.info('Summarization by content-diffbot: {0}'.format(article.get('url')))
                        res = requests.post("https://api.smmry.com?SM_API_KEY={0}".format(SM_API_KEY), data={'sm_api_input': content})
                        summarization = res.json().get('sm_api_content')
                        if summarization is None:
                            logging.error("Exception in summarization by content-diffbot: {0}".format(res.text))
                            if 'GO TO PARTNER PAGE FOR MORE' in res.text.upper():
                                logging.error("Need more smmry credits")
                                break

                    except Exception as ex:
                        logging.error("Exception in summarization by content-diffbot: {0}".format(content))
                        traceback.print_exc()
                        summarization = ""
                        if 'GO TO PARTNER PAGE FOR MORE' in str(ex).upper():
                            logging.error("Need more smmry credits")
                            break

            except Exception as ex:
                logging.error("Exception in summarization by url - diffbot: {0}".format(article.get('url')))
                traceback.print_exc()
                summarization = ""
                if 'GO TO PARTNER PAGE FOR MORE' in str(ex).upper():
                    logging.error("Need more smmry credits")
                    break

        if content is not None:
            collection.update_one({'_id': article['_id']},
            {'$set': {'summarization': summarization, 'content': content}}, True)
        else:
            collection.update_one({'_id': article['_id']},
            {'$set': {'summarization': summarization}}, True)
        logging.info('Summarization result: {0}'.format(summarization))
        # time.sleep(10)
        # logging.info("Sleep 10 seconds...")

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())



