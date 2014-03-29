__author__ = 'pwentrys'

from flask import Flask, render_template, url_for
import urllib2

app = Flask(__name__)

#localhost:1234 information setting for how to access site
LISTEN_IP = '0.0.0.0'
LISTEN_PORT = 1234

#route for index...when you go to localhost:1234 -> brings you to html
@app.route('/')
def index():
    return render_template('index.html')

#app route to another page -> localhost:1234/blasto
#this basically is setup to pull output of a site and put it into "content" block
@app.route('/blasto')
def andromeda():
    response = urllib2.urlopen('http://google.com')
    page_data = str(response.read())
    return render_template('blasto.html', page_data=page_data)

@app.after_request
def shutdown_session(response):
    return response

if __name__ == "__main__":
    app.run(host=LISTEN_IP, port=LISTEN_PORT, debug=True)
