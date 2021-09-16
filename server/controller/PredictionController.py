from fastapi import APIRouter

from server.entity.ChatLog import ChatLog

prediction_controller = APIRouter(prefix="/prediction")


@prediction_controller.post("/")
def get_prediction_result(chat_log: ChatLog):
    pass
