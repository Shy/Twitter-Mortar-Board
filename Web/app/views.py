from app import app
import get_tweets
@app.route('/')
@app.route('/index')
def index():
        return get_tweets.get()