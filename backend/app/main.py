from fastapi import FastAPI
from pydantic import BaseModel

from .analysis.static_analyzer import StaticAnalyzer
from .analysis.ml_embedder import CodeEmbedder
from .analysis.classifier import CodeIssueClassifier
from .analysis.issue_merger import IssueMerger, MLIssue

app = FastAPI()

# Initialize ML components once
embedder = CodeEmbedder()
classifier = CodeIssueClassifier()
merger = IssueMerger()


class AnalyzeRequest(BaseModel):
    file_path: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/analyze")
def analyze_file(req: AnalyzeRequest):
    file_path = req.file_path

    # --- 1. Static Analysis ---
    static_engine = StaticAnalyzer(file_path)
    static_issues = static_engine.analyze()

    # Read the file content for ML
    try:
        with open(file_path, "r") as f:
            code = f.read()
    except Exception as e:
        return {"error": f"Could not read file: {str(e)}"}

    # --- 2. ML Embeddings ---
    embedding = embedder.embed_code(code)

    # --- 3. ML Classification ---
    category = classifier.predict(embedding)
    ml_issue = MLIssue(
        file=file_path,
        line=0,
        category=category,
        confidence=0.50,  
        message=f"ML-detected potential issue: {category}",
    )

    # --- 4. Merge Results ---
    final_issues = merger.merge(static_issues, [ml_issue])

    return {"issues": final_issues}
