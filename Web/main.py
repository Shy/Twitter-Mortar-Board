import twitter

if __name__ == "__main__":
    config = {}
    execfile("config.conf", config)
    api = twitter.Api(consumer_key=config["consumer_key"],
                      consumer_secret=config["consumer_secret"],
                      access_token_key=config["access_token_key"],
                      access_token_secret=config["access_token_secret"])
    print api.VerifyCredentials()