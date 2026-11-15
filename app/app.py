import time
import redis
from flask import Flask
from redis import Redis

app = Flask(__name__)
cache = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = cache.incr('hits')
    return f'Hello Docker Compose! I have been seen {count} times.\n'
