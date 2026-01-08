from nlp.intent_classifier import predict_intent
from actions.reply_manager import get_reply
from actions.keyword_intents import KEYWORD_INTENTS

# clarification memory
LAST_PENDING_INTENT = None


def execute_action(text, context=None):
    global LAST_PENDING_INTENT
    context = context or {}

    text_l = text.lower().strip()

    # 🔹 KEYWORD RULES FIRST
    for keyword, intent in KEYWORD_INTENTS.items():
        if keyword in text_l:
            print("DEBUG keyword hit:", keyword, "->", intent)
            return {
                "intent": intent,
                "reply": get_reply(intent)
            }

    # 🔹 ML INTENT
    intent = predict_intent(text)
    print("DEBUG ML intent:", intent)

    # 🎯 CONTEXT-AWARE LOGIC (THIS IS WHAT WE TALKED ABOUT)
    if intent == "open_profile":
        if context.get("screen") == "chat_screen":
            return {
                "intent": "open_current_chat_profile",
                "reply": f"Opening {context.get('selected_user')}'s profile"
            }
        else:
            LAST_PENDING_INTENT = "open_profile"
            return {
                "intent": "clarify_profile",
                "reply": "Which profile do you want to open?"
            }

    # 🔁 FOLLOW-UP HANDLING
    if LAST_PENDING_INTENT == "open_profile":
        LAST_PENDING_INTENT = None
        return {
            "intent": "open_named_profile",
            "reply": f"Opening {text}'s profile"
        }

    return {
        "intent": intent,
        "reply": get_reply(intent)
    }
