import logging
import re

from df_engine.core.keywords import LOCAL, PROCESSING, TRANSITIONS, RESPONSE, GLOBAL
from df_engine.core import Actor
import df_engine.conditions as cnd
import df_engine.labels as lbl

import common.dff.integration.condition as int_cnd
import common.dff.integration.processing as int_prs
import common.dff.integration.response as int_rsp


import common.constants as common_constants

from . import condition as loc_cnd
from . import response as loc_rsp

logger = logging.getLogger(__name__)

# First of all, to create a dialog agent, we need to create a dialog script.
# Below, `flows` is the dialog script.
# A dialog script is a flow dictionary that can contain multiple flows .
# Flows are needed in order to divide a dialog into sub-dialogs and process them separately.
# For example, the separation can be tied to the topic of the dialog.
# In our example, there is one flow called greeting_flow.

# Inside each flow, we can describe a sub-dialog using keyword `GRAPH` from df_engine.core.keywords module.
# Here we can also use keyword `GLOBAL_TRANSITIONS`, which we have considered in other examples.

# `GRAPH` describes a sub-dialog using linked nodes, each node has the keywords `RESPONSE` and `TRANSITIONS`.

# `RESPONSE` - contains the response that the dialog agent will return when transitioning to this node.
# `TRANSITIONS` - describes transitions from the current node to other nodes.
# `TRANSITIONS` are described in pairs:
#      - the node to which the agent will perform the transition
#      - the condition under which to make the transition

flows = {
    GLOBAL: {
        TRANSITIONS: {
            ("greeting", "hi_node", 0.9): cnd.regexp(r"\b(مرحبا|اهلا|هاي| سلام\b )\b"),
            ("greeting", "how_bot_is_doing"): cnd.regexp(r"(كيف حالك|كيف أنت)"),
            ("greeting", "bye_node"): cnd.regexp(r"(إلى اللقاء|وداعا|مع السلامة)"),
            ("greeting", "what_bot_can_do"): cnd.regexp(r"(ماذا يمكنك أن تفعل|ماذا تفعل|ماذا تستطيع أن تفعل|ماذا تستطيع أن تفعل)")
        },
    },
    "sevice": {
        "start": {
            RESPONSE: "",
            TRANSITIONS: {
                ("greeting", "hi_node", 0.9): cnd.regexp(r"(مرحبا|اهلا|هاي|سلام)"),
                ("greeting", "how_bot_is_doing"): cnd.regexp(r"(كيف حالك|كيف أنت)"),
                ("greeting", "bye_node"): cnd.regexp(r"(إلى اللقاء|وداعا|مع السلامة)"),
                ("greeting", "what_bot_can_do"): cnd.regexp(r"(ماذا يمكنك أن تفعل|ماذا تفعل|ماذا تستطيع أن تفعل|ماذا تستطيع أن تفعل)")
            },
        },
        "fallback": {
            RESPONSE: "!لا أعرف كيف أجيب، ولكنني سأتعلم",
            TRANSITIONS: {
                lbl.previous(): cnd.regexp(r"previous", re.IGNORECASE),
                lbl.repeat(0.2): cnd.true(),
            },
        },
    },
    "greeting": {
        LOCAL: {
            PROCESSING: {
                # "set_confidence": int_prs.set_confidence(1.0),
                "set_can_continue": int_prs.set_can_continue(),
                # "fill_responses_by_slots": int_prs.fill_responses_by_slots(),
            },
        },
        "hi_node": {
            RESPONSE: "مرحبا! كيف حالك؟",
            PROCESSING: {
                "set_confidence": int_prs.set_confidence(0.9),
                "set_can_continue": int_prs.set_can_continue(),
                # "fill_responses_by_slots": int_prs.fill_responses_by_slots(),
            },
            TRANSITIONS: {
                "how_bot_is_doing": cnd.regexp(r"(كيف حالك|كيف أنت|وانت)"),
            },
        },
        "how_bot_is_doing": {
            RESPONSE: "!أنا بخير، شكرًا",
            PROCESSING: {},
            TRANSITIONS: {},
        },
        "bye_node": {
            RESPONSE: "!مع السلامة",
            PROCESSING: {},
            TRANSITIONS: {},
        },
        "what_bot_can_do": {
            RESPONSE: ".أعرف كيف أجيب على الأسئلة",
            PROCESSING: {},
            TRANSITIONS: {},
        }
    },
}


actor = Actor(flows, start_label=("sevice", "start"), fallback_label=("sevice", "fallback"))
