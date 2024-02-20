import json                                                     
from flask import Flask, request, jsonify                                
from transformers import AutoModelForCausalLM, AutoTokenizer

app = Flask(__name__)                                           

device = "cuda" # the device to load the model onto

model = AutoModelForCausalLM.from_pretrained("mistralai/Mixtral-8x7B-v0.1")
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mixtral-8x7B-v0.1")                                 

  
@app.route("/", methods=['POST'])
def receive_json():
    if not request.is_json:
        return jsonify({"error": "No JSON data found in request"}), 400
    try:
        messages = request.get_json()
        
    except Exception as e:
        return jsonify({"error": "Invalid JSON format"}), 400
    
    text = tokenizer.apply_chat_template(
            [messages],
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

    return response          
    
if __name__ == '__main__': 
   app.run(debug = True) 

