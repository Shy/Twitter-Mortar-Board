import os
import get_tweets
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        return get_tweets.get()
    except:
        return "refresh"
