from fastapi import APIRouter

from server.entity.ChatLog import ChatLog
from server.entity.ChatMessage import ChatMessage
from server.entity.ToxicityAnalysisResult import ToxicityAnalysisResult
from server.service.ToxicityAnalysisService import ToxicityAnalysisService

toxicity_analysis_controller = APIRouter(prefix="/toxicity-analysis")


@toxicity_analysis_controller.post("/", response_model=ToxicityAnalysisResult)
def get_prediction_result(chat_message: ChatMessage) -> ToxicityAnalysisResult:
    return ToxicityAnalysisService.analyze_message(chat_message)
