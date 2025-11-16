from transformers import AutoTokenizer, AutoModel
import torch


class CodeEmbedder:
    """Generates embeddings for code using a pretrained transformer model."""

    def __init__(self, model_name: str = "microsoft/codebert-base"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)

    def embed_code(self, code: str):
        """Return a vector embedding for the given code snippet."""
        inputs = self.tokenizer(code, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            outputs = self.model(**inputs)
            embedding = outputs.last_hidden_state.mean(dim=1)  # average pooling
        return embedding.squeeze().numpy()
