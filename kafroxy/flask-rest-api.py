from flask import Flask
from flask import json
from flask import request
from kafka import KafkaProducer
from flask_cors import CORS
from survey import Survey
import csv
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


@app.route('/survey', methods=['GET'])
def survey():

    with open(config.csv, 'rt', encoding='utf-8') as csvFile:

        reader = csv.reader(csvFile, delimiter=',')

        surveys = []

        for row in reader:
            survey_id = row[0]
            survey_code = row[1]
            question_id = row[2]
            question_handle = row[3]
            question_short_code = row[4]
            scale_id = row[5]
            scale_handle = row[6]
            answer_id = row[7]
            answer_handle = row[8]
            answer_weight = row[9]
            answer_data_type = row[10]
            value = row[11]
            question_text = row[12]
            answer_text = row[13]

            survey = Survey(survey_id,
                            survey_code,
                            question_id,
                            question_handle,
                            question_short_code,
                            scale_id,
                            scale_handle,
                            answer_id,
                            answer_handle,
                            answer_weight,
                            answer_data_type,
                            value,
                            question_text,
                            answer_text)

            surveys.append(survey)

        result = json.dumps([ob.__dict__ for ob in surveys])

        return result

if __name__ == '__main__':
    app.run()
