from flask import Flask
import redis

app = Flask(__name__)

# Connect to Redis (running in a separate container)
redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def home():
    # Increment the visit count in Redis
    count = redis_client.incr('visits')
    return f'Hello, Docker! You have visited this page {count} times.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
