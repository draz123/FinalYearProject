import sys
import os
import time
import datetime

from twitter import *

class TwitterPostDownloader:

    def __init__(self):
        self.creditionals= ['JEdRRoDsfwzCtupkir4ivQ' , 'PAbSSmzQxbcnkYYH2vQpKVSq2yPARfKm0Yl6DrLc']

    def getTweetFromTwitter(self,tweetID):
        MY_TWITTER_CREDS = os.path.expanduser('~/.my_app_credentials')
        if not os.path.exists(MY_TWITTER_CREDS):
            oauth_dance("Crime analyze", self.creditionals[0], self.creditionals[1], MY_TWITTER_CREDS)
        oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)
        t = Twitter(auth=OAuth(oauth_token, oauth_secret, self.creditionals[0], self.creditionals[1]))
        cache = {}
        while not tweetID in cache:
            try:
                text = t.statuses.show(_id=tweetID)['text'].replace('\n', ' ').replace('\r', ' ')
                cache[tweetID] = text
            except TwitterError as e:
                if e.e.code == 429:
                    rate = t.application.rate_limit_status()
                    reset = rate['resources']['statuses']['/statuses/show/:id']['reset']
                    now = datetime.datetime.today()
                    future = datetime.datetime.fromtimestamp(reset)
                    seconds = (future-now).seconds+1
                    if seconds < 10000:
                        sys.stderr.write("Rate limit exceeded, sleeping for %s seconds until %s\n" % (seconds, future))
                        time.sleep(seconds)
                else:
                    cache[tweetID] = 'Not Available'

        text = cache[tweetID]
        # with open('downloaded_post.tsv', 'w') as f:
        #     f.write(text)
        return text

# if __name__ == '__main__':
#     t=TwitterPostDownloader()
#     tweetID=817189049773473793
#     print t.getTweetFromTwitter(tweetID)