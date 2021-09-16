from typing import List
from pydantic import BaseModel

from server.entity.ChatMessage import ChatMessage


class ChatLog(BaseModel):
    messages: List[ChatMessage]
