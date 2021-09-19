from typing import Dict, List

from pydantic import BaseModel


class QuestBase(BaseModel):
    id: int
    name: str
    description: str
    starting_segment: int
    variables: Dict[str, str]
    initial_values: Dict[str, int]


class QuestSegmentBase(BaseModel):
    id: int
    quest_id: int
    text: str
    text_ru: str


class QuestSegmentRelationBase(BaseModel):
    id: int
    quest_id: int
    from_segment_id: int
    to_segment_id: int
    is_random: bool
    is_typed: bool
    action_text: str
    action_text_ru: str
    predicate: Dict[str, str]
    effects: Dict[str, str]
