from pydantic import BaseModel
from typing import List, Dict


class CorrectorRequest(BaseModel):
    headers: Dict[str, str]
    texts: List[str]


class CorrectedResult(BaseModel):
    result: Dict[str, str]
