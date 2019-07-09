from flask import Flask
app = Flask(__name__)

import nexmo
client = nexmo.Client(
	application_id='ea53dec3-c930-4333-a9e5-bb97e9e662d7',
	private_key='private.key',
)

from pprint import pprint

@app.route("/")
def hello():
	response = client.create_call({
	'to': [{'type': 'phone', 'number': '33781639678'}],
	'from': {'type': 'phone', 'number': '33644633287'},
	'answer_url': ['https://developer.nexmo.com/ncco/tts.json']
	})
    pprint(response)
	
