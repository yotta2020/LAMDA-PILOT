import torch
import torch.nn as nn
from transformers import AutoModel, AutoTokenizer

class CodePretrainedModel(nn.Module):
    """Base class for code domain pre-trained models"""
    def __init__(self, model_name, max_length=512):
        super().__init__()
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
        self.max_length = max_length
        
    def forward(self, code_inputs):
        # Tokenize inputs
        inputs = self.tokenizer(
            code_inputs,
            padding=True,
            truncation=True,
            max_length=self.max_length,
            return_tensors="pt"
        ).to(self.model.device)
        
        # Get model outputs
        outputs = self.model(**inputs)
        
        return {
            'features': outputs.last_hidden_state[:, 0, :],  # [CLS] token
            'hidden_states': outputs.hidden_states if hasattr(outputs, 'hidden_states') else None
        }
