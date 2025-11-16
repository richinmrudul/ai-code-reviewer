import numpy as np
from sklearn.linear_model import LogisticRegression


class CodeIssueClassifier:
    """
    Simple ML classifier that predicts the category of an issue
    based on the CodeBERT embedding.
    """

    def __init__(self):
        # Placeholder: untrained model
        
        self.model = LogisticRegression()
        self.is_trained = False

    def train(self, embeddings: np.ndarray, labels: np.ndarray):
        """Train the classifier."""
        self.model.fit(embeddings, labels)
        self.is_trained = True

    def predict(self, embedding: np.ndarray) -> str:
        """Predict issue type from embedding."""
        if not self.is_trained:
            # Fallback prediction — MVP mode
            return "ML_Issue (untrained)"
        
        pred = self.model.predict([embedding])[0]
        return pred
