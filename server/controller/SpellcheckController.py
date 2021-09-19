import json
from typing import List

from fastapi import APIRouter, Depends
from pydantic.main import BaseModel
from sqlalchemy.orm import Session

from ..converters import quest_relation_converter, quest_segment_converter, quest_converter
from ..schemas import QuestBase, QuestSegmentBase, QuestSegmentRelationBase
from ..spellchecker.tatdistrsem import TatSpellCheck
from ..utils import get_session
from .. import crud

spellcheck_controller = APIRouter(prefix="/spellcheck")
tst = TatSpellCheck()


class ResultModel(BaseModel):
    has_error: bool
    error_index: int
    word: str


@spellcheck_controller.post("/", response_model=ResultModel)
def fap(
        text: str
):
    spr = tst.spellcheck(text)
    data_set = {
        "has_error": False if spr[0] == 0 else True,
        "error_index": spr[0] - 1,
        "word": spr[1]
    }
    print(data_set)
    return ResultModel(**data_set)
