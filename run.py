import tweepy
import time, config, os
cwd = os.getcwd()

CONSUMER_KEY = config.consumerKey
CONSUMER_SECRET = config.consumerSecret
ACCESS_KEY = config.accessToken
ACCESS_SECRET = config.accessSecret

auth = tweepy.OAuthHandler(CONSUMER_KEY , CONSUMER_SECRET)

auth.set_access_token(ACCESS_KEY , ACCESS_SECRET)

api = tweepy.API(auth)

word = config.keyword
try:
    file_list = "text.txt"
    myfile = open(f"{cwd}/{file_list}","r",encoding="utf-8")
    text = myfile.read()
except:
    pass
nrTweets = 10
print(f" ============ AUTO RETWEET / REPLY BY RJD ============")
validator = []
while True:
    try:
        for tweet in tweepy.Cursor(api.search, word).items(nrTweets):
            try:
                print(f"[{time.strftime('%d-%m-%y %X')}] Searching New Tweet 10s...")
                # api.retweet(tweet.id)
                if len(text) == 0:
                    api.retweet(tweet.id)
                    print(f"[{time.strftime('%d-%m-%y %X')}] Retweet Bot Found Tweet by @{tweet.user.screen_name}: {tweet.text} ")
                    print(f"[{time.strftime('%d-%m-%y %X')}] Retweet Succesfully.")

                else:
                    if tweet.id in validator:
                        pass
                    else:
                        tweet_to_quote_url=f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"
                        api.update_status(text, attachment_url=tweet_to_quote_url)
                        print(f"[{time.strftime('%d-%m-%y %X')}] Retweet Bot Found Tweet by @{tweet.user.screen_name}: {tweet.text} ")
                        print(f"[{time.strftime('%d-%m-%y %X')}] Retweet and Quote Succesfully.")
                        validator.append(tweet.id)

                # Quote it in a new status

                print(f"[{time.strftime('%d-%m-%y %X')}] Wait For 10s...")
                time.sleep(10)
            except Exception as e:
                if "Forbidden duplicate" in str(e) or "already" in str(e) or "404" in str(e) or "144" in str(e) or "187" in str(e):
                    pass
                else:
                     print(f"[{time.strftime('%d-%m-%y %X')}] Error: {e}")
                time.sleep(10)

    except Exception as e:
        print(f"[{time.strftime('%d-%m-%y %X')}] Error: {e}")
        quit()
