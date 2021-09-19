from typing import TypedDict
from sqlalchemy import Column, String, Integer, Boolean
from .database import Base

class Quest(Base):
    __tablename__ = "quests"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    starting_segment = Column(Integer)
    variables = Column(String)
    initial_values = Column(String)

class QuestSegment(Base):
    __tablename__ = "segments"
    id = Column(Integer, primary_key=True)
    quest_id = Column(Integer)
    text = Column(String)
    text_ru = Column(String)

class QuestSegmentRelation(Base):
    __tablename__ = "relations"
    id = Column(Integer, primary_key=True)
    quest_id = Column(Integer)
    from_segment_id = Column(Integer)
    to_segment_id = Column(Integer)
    is_random = Column(Boolean)
    is_typed = Column(Boolean)
    action_text = Column(String)
    action_text_ru = Column(String)
    predicate = Column(String)
    effects = Column(String)