import ast
from dataclasses import dataclass
from typing import List

@dataclass
class Issue:
    file: str
    line: int
    type: str
    message: str
