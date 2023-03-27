import logging
from os import getenv
import json
import requests

from df_engine.core import Context, Actor

ODQA_SERVICE_URL = getenv("ODQA_SERVICE_URL")


logger = logging.getLogger(__name__)
# ....


def example_response(reply: str):
    def example_response_handler(ctx: Context, actor: Actor, *args, **kwargs) -> str:
        return reply

    return example_response_handler


def odqa_response():
    def odqa_response_handler(ctx: Context, actor: Actor, *args, **kwargs) -> str:
        processed_node = ctx.last_request
        request_data = {"question_raw": [processed_node]}
        result = requests.post(ODQA_SERVICE_URL, json=request_data).json()
        if result[1][0] < 0.7:
            return "!لا أعرف كيف أجيب، ولكنني سأتعلم"
        return result[0][0]

    return odqa_response_handler
