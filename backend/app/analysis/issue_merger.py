from typing import List
from dataclasses import dataclass
from .static_analyzer import Issue as StaticIssue


@dataclass
class MLIssue:
    file: str
    line: int
    category: str
    confidence: float
    message: str


class IssueMerger:
    """
    Combines static analysis issues + ML issues into a single unified list.
    """

    def __init__(self):
        pass

    def merge(self, static_issues: List[StaticIssue], ml_issues: List[MLIssue]):
        """
        Returns one final list containing both static and ML issues.
        """
        combined = []

        # Convert StaticIssue dataclass to a dict-like output
        for issue in static_issues:
            combined.append({
                "source": "static",
                "file": issue.file,
                "line": issue.line,
                "type": issue.type,
                "message": issue.message,
                "confidence": None
            })

        # Add ML issues
        for ml in ml_issues:
            combined.append({
                "source": "ml",
                "file": ml.file,
                "line": ml.line,
                "type": ml.category,
                "message": ml.message,
                "confidence": ml.confidence
            })

        return combined
