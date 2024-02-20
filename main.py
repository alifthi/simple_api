import json                                                     
from flask import Flask, request, jsonify                                
from transformers import AutoModelForCausalLM, AutoTokenizer

app = Flask(__name__)                                           

device = "cuda" # the device to load the model onto

model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen1.5-7B-Chat",
    device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen1.5-7B-Chat")                                       

  
@app.route("/", methods=['POST'])
def receive_json():
    if not request.is_json:
        return jsonify({"error": "No JSON data found in request"}), 400
    try:
        messages = request.get_json()
    except Exception as e:
        return jsonify({"error": "Invalid JSON format"}), 400
    prompts=messages['message']
    text = tokenizer.apply_chat_template(
            [prompts],
        tokenize=False,
        add_generation_prompt=True)
    model_inputs = tokenizer([text], return_tensors="pt").to(device)

    generated_ids = model.generate(
    model_inputs.input_ids,
        max_new_tokens=512
	    )
    generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)]

    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    is_first_message=messages['is_first_message']
    language=messages['lang']
    return jsonify({'response':response})          
    
if __name__ == '__main__': 
   app.run(debug = True) 

