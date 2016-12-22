from flask import Flask
from flask import json
from flask import request
from kafka import KafkaProducer
from flask_cors import CORS


import config

app = Flask(__name__)
CORS(app)

producer = KafkaProducer(bootstrap_servers=config.brokers)


@app.route('/ping', methods=['GET'])
def ping():
    return 'pong'


@app.route('/', methods=['POST'])
def create():

    json_dict = request.get_json()

    print('respondentUniqueKey: ' + json_dict['respondentUniqueKey'])

    json_message = json.dumps(json_dict)

    print(json_message)

    key = json_dict['respondentUniqueKey'].encode('utf8')

    value = str.encode(json_message)

    producer.send(config.topic, key=key, value=value)

    return json_message

if __name__ == '__main__':
    app.run()
