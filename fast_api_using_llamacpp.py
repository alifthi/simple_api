import json
from fastapi import FastAPI, Request, Response, status
from utils import model, prompt
app = FastAPI()

print('Tokenizer loaded ...')
model=model()
prompt=prompt()
@app.post("/")
async def receive_json(request: Request):
    try:
        messages = await request.json()
    except Exception as e:
        return Response(content=json.dumps({"error": "Invalid JSON format"}), status_code=status.HTTP_400_BAD_REQUEST)
    # To Do
    if messages['is_first_message']:
        response=prompt.fistMessage(messages)
        if response=='yes':
            # Do some thing
            pass
        response=prompt.extractNER(messages)
        # Do some things on android phone
        return  
    response=model.generate(messages)
    return Response(content=json.dumps({"response": response}), status_code=status.HTTP_200_OK)

