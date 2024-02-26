class prompt:
    def __init__(self) -> None:
        pass
    def fistMessage(self,message): 
        return f' <|im_start|> is this massage wants some thing about android phone? just say yes or no:\n{message}<|im_end|> <|im_start|>assistant' 
    def extractNER(self,response):
        prompt=f"<|im_start|> Extract the all entities of the following sentence **say the entities like a json\n {response} <|im_end|> <|im_start|>assistant"
        return prompt