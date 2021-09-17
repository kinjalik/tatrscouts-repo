from detoxify import Detoxify
from server.entity.ChatMessage import ChatMessage
from server.entity.ToxicityAnalysisResult import ToxicityAnalysisResult


class ToxicityAnalysisService:
    @staticmethod
    def analyze_message(chat_message: ChatMessage):
        text = chat_message.text
        toxic_coef = Detoxify('multilingual').predict(text)['toxicity']
        verdict = "neutral"

        if toxic_coef < 0.001:
            verdict = 'positive'
        elif toxic_coef > 0.08 and toxic_coef < 0.5:
            verdict = 'negative'
        elif toxic_coef >= 0.5:
            verdict = 'very negative'

        result = {
            "text": text,
            "toxicity_coefficient": toxic_coef,
            "verdict": verdict
        }
        return ToxicityAnalysisResult(**result)
