from llama_cpp import Llama  
import json
from fastapi import FastAPI, Request, Response, status
from transformers import AutoModelForCausalLM, AutoTokenizer
import time
app = FastAPI()

device = "cpu" # the device to load the model onto
model_id="Qwen/Qwen1.5-7B-Chat"
model="./models/qwen1_5-14b-chat-q5_k_m.gguf"

llm = Llama(model_path=model, n_ctx=8192, n_threads=8, n_batch=512, n_gpu_layers=2, verbose=True, seed=42)

tokenizer = AutoTokenizer.from_pretrained(model_id)
print('Tokenizer loaded ...')

@app.post("/")
async def receive_json(request: Request):
    try:
        messages = await request.json()
    except Exception as e:
        return Response(content=json.dumps({"error": "Invalid JSON format"}), status_code=status.HTTP_400_BAD_REQUEST)
    response = generate(messages)
    return Response(content=json.dumps({"response": response}), status_code=status.HTTP_200_OK)

def generate(messages):
    print(messages)
    user=messages['message']
    message=f' <|im_start|>{user}<|im_end|> <|im_start|>assistant'
    output = llm(message, echo=True, stream=False, max_tokens=512) 
    output = output['choices'][0]['text'].replace(message, '')
    return output











