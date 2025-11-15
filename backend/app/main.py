from fastapi import FastAPI

app = FastAPI(title="AI Code Reviewer", version="0.1.0")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/analyze")
def analyze_code():
    """
    TODO:
    - Accept code input (file path, raw string, or repo ref)
    - Run static analyzer (AST-based)
    - Run ML embedder + classifier
    - Merge issues and return unified report
    """
    return {"message": "analysis pipeline not implemented yet"}
