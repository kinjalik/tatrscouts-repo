from typing import List

from sqlalchemy.orm import Session  # type: ignore

from .models import Quest, QuestSegment, QuestSegmentRelation


def get_quests(session: Session, skip: int = 0, limit: int = 100) -> List[Quest]:
    return session \
        .query(Quest) \
        .offset(skip) \
        .limit(limit) \
        .all()


def get_segments_by_quest_id(session: Session, quest_id: int) -> List[QuestSegment]:
    return session \
        .query(QuestSegment) \
        .filter(QuestSegment.quest_id == quest_id) \
        .all()


def get_relations_to_segment_id(session: Session, quest_id: int, to_seg_id: int) -> List[QuestSegmentRelation]:
    return session \
        .query(QuestSegmentRelation) \
        .filter(QuestSegmentRelation.quest_id == quest_id) \
        .filter(QuestSegmentRelation.to_segment_id == to_seg_id) \
        .all()


def get_relation_from_segment_id(session: Session, quest_id: int, from_seg_id: int) -> List[QuestSegmentRelation]:
    return session \
        .query(QuestSegmentRelation) \
        .filter(QuestSegmentRelation.quest_id == quest_id) \
        .filter(QuestSegmentRelation.from_segment_id == from_seg_id) \
        .all()
