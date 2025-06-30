from smolagents.models.base import BaseModel

class OllamaModel(BaseModel):
    def __init__(self, model_name="deepseek-r1:14b", temperature=0.1, max_tokens=1024):
        import ollama
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.ollama = ollama

    def complete(self, prompt, **kwargs):
        response = self.ollama.generate(
            model=self.model_name,
            prompt=prompt,
            options={
                "temperature": self.temperature,
                "num_predict": self.max_tokens
            }
        )
        return response['response']
