from llama_cpp import Llama  
from transformers import  AutoTokenizer
class prompt:
    def __init__(self) -> None:
        pass
    def fistMessage(self,chat): 
        response=chat[-1]['content']
        prompt=[{"role": "system", "content": "You are an assistant who perfectly describes images."},
                {'role':'user','content':f'is the following sentence want some thing in mobile phone? just say yes or no:\n{response}'}]
        return prompt
    def extractNER(self,chat):
        response=chat[-1]['content']
        prompt=[{"role": "system", "content": "You are an assistant who perfectly describes images."},
                {'role':'user','content':f'Extract the entities of the following sentence **say the entities like a json\n {response}'}]
        return prompt
class model:
    def __init__(self, modelId="Qwen/Qwen1.5-7B-Chat",
                 modelPath='./models/qwen1_5-14b-chat') -> None:
        self.model=Llama(model_path=modelPath, n_ctx=8192, n_threads=8, n_batch=512, n_gpu_layers=2, verbose=True, seed=42)
        self.tokenizer=AutoTokenizer.from_pretrained(modelId)
    def generate(self,messages):
        message=messages['chat']
        
        output = self.model.create_chat_completion(message, echo=True, stream=False, max_tokens=512) 
        output = output['choices'][0]['text'].replace(message, '')
        return output
