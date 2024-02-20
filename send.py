import requests
import json

data = {"name": "Alice", "age": 30}

headers = {"Content-Type": "application/json"}
prompt="Do NER on the following text without more explenation: \n set alarm for 9:30"
messages = {'lang':'persian','is_first_message':True,'message':{"role": "user", "content": prompt}}
messages=json.dumps(messages)
response = requests.post("http://localhost:5000/", data=messages, headers=headers)

if response.status_code == 200:
    response=response.json()
    response=response['response']
    print("JSON file sent successfully!",response)
else:
    print("Error sending file:", response.content.decode())
