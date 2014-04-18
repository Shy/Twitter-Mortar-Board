if __name__ == "__main__":
    config = {}
    execfile("config.conf", config)

    print config["consumer_key"]
    print config["consumer_secret"]
    print config["access_token_key"]
    print config["access_token_secret"]