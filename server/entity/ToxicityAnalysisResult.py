from typing import Mapping
from pydantic import BaseModel


class ToxicityAnalysisResult(BaseModel):
    text: str
    toxicity_coefficient: float
    verdict: str
