
import json
from fastapi import FastAPI, Request, Response, status

app = FastAPI()

device = "cpu" # the device to load the model onto
model_id = "mistralai/Mistral-7B-Instruct-v0.1"
# model_id = "mistralai/Mixtral-8x7B-v0.1"
model = AutoModelForCausalLM.from_pretrained(model_id)
print('model loaded...')
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
    prompts = messages["message"]
    text = tokenizer.apply_chat_template(
    [prompts],
    tokenize=False,
    add_generation_prompt=True)
    model_inputs = tokenizer([text], return_tensors="pt").to(device)
    print('tokenized....')
    generated_ids = model.generate(
    model_inputs.input_ids,
    max_new_tokens=512)
    print('generated...')
    generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)]

    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    is_first_message = messages["is_first_message"]
    language = messages["lang"]
    return response