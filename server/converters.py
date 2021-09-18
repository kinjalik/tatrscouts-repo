import json

from server.models import QuestSegmentRelation, QuestSegment
from server.schemas import QuestSegmentRelationBase, QuestSegmentBase


def quest_segment_converter(alchemy: QuestSegment) -> QuestSegmentBase:
    d = alchemy.__dict__
    return QuestSegmentBase(**d)


def quest_relation_converter(alchemy: QuestSegmentRelation) -> QuestSegmentRelationBase:
    d = alchemy.__dict__
    d['predicate'] = json.loads(d['predicate'])
    return QuestSegmentRelationBase(**d)
