import json
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..converters import quest_relation_converter, quest_segment_converter
from ..schemas import QuestBase, QuestSegmentBase, QuestSegmentRelationBase
from ..utils import get_session
from .. import crud

quest_controller = APIRouter(prefix="/quests")


@quest_controller.get("/", response_model=List[QuestBase])
def get_quest_list(
        session: Session = Depends(get_session)
):
    quests = crud.get_quests(session=session)
    result = []
    for q in quests:
        qDict = q.__dict__
        qDict['variables'] = json.loads(qDict['variables'])
        result.append(QuestBase(**qDict))
    return result


@quest_controller.get("/{quest_id}/segments", response_model=List[QuestSegmentBase])
def get_quest_segments(
        quest_id: int,
        session: Session = Depends(get_session)
):
    segments = crud.get_segments_by_quest_id(session, quest_id)
    return [quest_segment_converter(q) for q in segments]

@quest_controller.get("/{quest_id}/relations/from/{segment_id}", response_model=List[QuestSegmentRelationBase])
def get_quest_relations_from_segment(
        quest_id: int,
        segment_id: int,
        session: Session = Depends(get_session)
):
    segments = crud.get_relation_from_segment_id(session, quest_id, segment_id)
    return [quest_relation_converter(q) for q in segments]

@quest_controller.get("/{quest_id}/relations/to/{segment_id}", response_model=List[QuestSegmentRelationBase])
def get_quest_relations_to_segment(
        quest_id: int,
        segment_id: int,
        session: Session = Depends(get_session)
):
    segments = crud.get_relations_to_segment_id(session, quest_id, segment_id)
    return [quest_relation_converter(q) for q in segments]