import requests
import json
import time 
headers = {"Content-Type": "application/json"}
prompt="چطور میتونم سرعت اجرا یه برنامه رو افزایش بدم؟"
messages = {'lang':'persian','is_first_message':True,'message':
			{"role": "user", "content":prompt}}
messages=json.dumps(messages)
a=time.time()
response = requests.post("http://79.127.125.211:44580", data=messages, headers=headers)

if response.status_code == 200:
    response=response.json()
    response=response['response']
    print(f'response recived in {time.time()-a} s',response)
else:
    print("Error sending file:", response.content.decode())
