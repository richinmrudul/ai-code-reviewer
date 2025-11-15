from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from .analysis.static_analyzer import StaticAnalyzer, Issue

app = FastAPI(title="AI Code Reviewer", version="0.2.0")


class AnalyzeRequest(BaseModel):
    file_path: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/analyze")
def analyze_code(request: AnalyzeRequest):
    """
    Accepts a file path, runs static analysis, and returns issues.
    """
    analyzer = StaticAnalyzer(request.file_path)
    issues: List[Issue] = analyzer.analyze()

    return {
        "file": request.file_path,
        "issues": [issue.__dict__ for issue in issues],
    }
