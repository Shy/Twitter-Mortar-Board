import tweepy
import sys

if __name__ == "__main__":
    config = {}
    execfile("config.conf", config)

    auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
    auth.set_access_token(config["access_token_key"], config["access_token_secret"])

    api = tweepy.API(auth)


    tweets = api.search(q='#UCgrad14',result_type='mixed')
    for tweet in tweets:
        try:
            if not ('RT @' in tweet.text):
                print "@" + tweet.user.screen_name +": " +tweet.text
        except:
            # print sys.exc_info()[0]
            i = 0