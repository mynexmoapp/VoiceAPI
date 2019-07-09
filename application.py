from flask import Flask
app = Flask(__name__)

import nexmo
from pprint import pprint

client = nexmo.Client(
	application_id='ea53dec3-c930-4333-a9e5-bb97e9e662d7',
	private_key='private.key',
)



response = client.create_call({
  'to': [{'type': 'phone', 'number': TO_NUMBER}],
  'from': {'type': 'phone', 'number': NEXMO_NUMBER},
  'answer_url': ['https://developer.nexmo.com/ncco/tts.json']
})

pprint(response)
	
