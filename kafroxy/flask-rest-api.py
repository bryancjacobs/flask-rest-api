from flask import Flask
from flask import json
from flask import request
from kafka import KafkaProducer

import config

app = Flask(__name__)


producer = KafkaProducer(bootstrap_servers=config.brokers)


@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'


@app.route('/', methods=['POST'])
def create():

    print(request.json)

    json_message = json.dumps(request.json)

    producer.send('test-message', str.encode(json_message))

    return json_message

if __name__ == '__main__':
    app.run()
