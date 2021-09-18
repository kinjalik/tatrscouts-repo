from typing import Dict, List

from pydantic import BaseModel


class QuestBase(BaseModel):
    id: int
    name: str
    description: str
    starting_segment: int
    variables: Dict[str, str]


class QuestSegmentBase(BaseModel):
    id: int
    quest_id: int
    text: str


class QuestSegmentRelationBase(BaseModel):
    id: int
    quest_id: int
    from_segment_id: int
    to_segment_id: int
    action_text: str
    predicate: List[str]
