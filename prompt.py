class prompt:
    def __init__(self) -> None:
        pass
    def fistMessage(self,message): 
        return f' <|im_start|> is this massage wants some thing about android phone? just say yes or no:\n{message}<|im_end|> <|im_start|>assistant'
    def relatedToPhone(self,message):
        return f'<|im_start|> Do NER task on the following message:\n{message}<|im_end|> <|im_start|>assistant' 
    def extractNER(self,response):
        pass