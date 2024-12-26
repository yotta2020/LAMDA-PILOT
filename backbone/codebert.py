from .code_models import CodePretrainedModel

class CodeBERT(CodePretrainedModel):
    """CodeBERT model for code understanding tasks"""
    def __init__(self, pretrained=True, max_length=512):
        model_name = "microsoft/codebert-base"
        super().__init__(model_name=model_name, max_length=max_length)
        self.out_dim = self.model.config.hidden_size  # 768 for base model
        
    @property
    def last_layer(self):
        """Return the last layer of the model for gradient computation"""
        return self.model.encoder.layer[-1]
