from flask import Flask,render_template,Response,request
import feedparser
import random

app = Flask(__name__)
rss_url = 'http://feeds.bbci.co.uk/news/world/rss.xml'
feed = feedparser.parse('http://feeds.bbci.co.uk/news/world/rss.xml')


@app.route("/")
def hello_world():
    randomnum = random.choice(range(2, 21))
    posts = feed.entries[randomnum].title
    postlink = feed.entries[randomnum].link
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()

    if "iphone" in user_agent:
        return render_template('mobile.home.html',posts=posts,postlink=postlink)
    elif "android" in user_agent:
        return render_template('mobile.home.html',posts=posts,postlink=postlink)
    else:
        return render_template('home.html',posts=posts,postlink=postlink)

if __name__== "__main__":
    app.run(debug=True)
