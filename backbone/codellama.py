import torch
import torch.nn as nn
from transformers import AutoModelForCausalLM, AutoTokenizer

class CodeLlama(nn.Module):
    """CodeLlama model for code understanding tasks"""
    def __init__(self, model_size="7b", max_length=512):
        super().__init__()
        model_name = f"codellama/CodeLlama-{model_size}-hf"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            device_map="auto"
        )
        self.max_length = max_length
        self.out_dim = self.model.config.hidden_size
        
    def forward(self, code_inputs):
        inputs = self.tokenizer(
            code_inputs,
            padding=True,
            truncation=True,
            max_length=self.max_length,
            return_tensors="pt"
        ).to(self.model.device)
        
        with torch.no_grad():
            outputs = self.model(**inputs, output_hidden_states=True)
        
        return {
            'features': outputs.hidden_states[-1][:, 0, :],  # Last layer [CLS] token
            'hidden_states': outputs.hidden_states
        }
        
    @property
    def last_layer(self):
        """Return the last layer of the model"""
        return self.model.model.layers[-1]