import logging
import sys

from server import config
from server.database import SessionLocal


def get_logger(name: str):
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(config.logs.fmt))
    handler.setLevel(config.logs.level)
    handler.setStream(sys.stdout)
    logger = logging.getLogger(name)
    logger.addHandler(handler)
    logger.setLevel(config.logs.level)
    return logger

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
