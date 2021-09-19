import json

from server.models import QuestSegmentRelation, QuestSegment, Quest
from server.schemas import QuestSegmentRelationBase, QuestSegmentBase, QuestBase


def quest_converter(q: Quest) -> QuestBase:
    qDict = q.__dict__
    qDict['variables'] = json.loads(qDict['variables'])
    qDict['initial_values'] = json.loads(qDict['initial_values'])
    return QuestBase(**qDict)


def quest_segment_converter(alchemy: QuestSegment) -> QuestSegmentBase:
    d = alchemy.__dict__
    return QuestSegmentBase(**d)


def quest_relation_converter(alchemy: QuestSegmentRelation) -> QuestSegmentRelationBase:
    d = alchemy.__dict__
    d['predicate'] = json.loads(d['predicate'])
    print(d)
    d['effects'] = json.loads(d['effects'])
    return QuestSegmentRelationBase(**d)
