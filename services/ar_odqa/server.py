import logging
import os
import time
from flask import Flask, request, jsonify
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from deeppavlov import build_model

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

config_name = os.getenv("CONFIG")

try:
    odqa = build_model(config_name)
    test_res = odqa(["""من هي صوفي فيليبين الفرنسية؟"""])
    # if test_res == [['كانت أميرة فرنسية'], [1.0], [70]]:
    logger.info(f"test: {test_res}")
except Exception as e:
    logger.exception(e)
    raise e

app = Flask(__name__)

@app.route("/ping", methods=["POST"])
def ping():
    return "pong"

@app.route("/model", methods=["POST"])
def respond():
    question = request.json.get("question_raw", [" "])
    try:
        tm_st = time.time()
        qa_res = odqa(question)
        logger.info(qa_res)
        # qa_res = [[elem[i] for elem in qa_res] for i in range(len(qa_res[0]))]
        logger.info(f"ar_odqa exec time: {time.time() - tm_st}")
    except Exception as e:
        logger.exception(e)
    return jsonify(qa_res)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=3000)
