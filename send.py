import requests
import json

data = {"name": "Alice", "age": 30}

headers = {"Content-Type": "application/json"}
prompt="Do NER on the following text without any explenation: \n set alarm for 9:30"
messages = {"role": "user", "content": prompt}
messages=json.dumps(messages)
response = requests.post("http://localhost:5000/", data=messages, headers=headers)

if response.status_code == 200:
    response=response.text
    print("JSON file sent successfully!",response)
else:
    print("Error sending file:", response.content.decode())
