import ast
from dataclasses import dataclass
from typing import List


@dataclass
class Issue:
    file: str
    line: int
    type: str
    message: str


class StaticAnalyzer:
    def __init__(self, file_path: str, max_function_length: int = 50):
        self.file_path = file_path
        self.max_function_length = max_function_length
        self.issues: List[Issue] = []

    def analyze(self) -> List[Issue]:
        """Parse file → AST → run checks"""
        try:
            with open(self.file_path, "r") as f:
                file_content = f.read()
        except FileNotFoundError:
            self.issues.append(
                Issue(
                    file=self.file_path,
                    line=0,
                    type="FileNotFound",
                    message="The file could not be found.",
                )
            )
            return self.issues

        tree = ast.parse(file_content)
        self._check_long_functions(tree)

        return self.issues

    def _check_long_functions(self, tree: ast.AST):
        """Detect functions longer than the limit."""
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if hasattr(node, "body") and node.body:
                    start_line = node.lineno
                    end_line = node.body[-1].lineno
                    length = end_line - start_line + 1

                    if length > self.max_function_length:
                        self.issues.append(
                            Issue(
                                file=self.file_path,
                                line=node.lineno,
                                type="LongFunction",
                                message=f"Function '{node.name}' is {length} lines long (limit {self.max_function_length}).",
                            )
                        )
