from actions.action_engine import execute_action

tests = [
    # keyword-driven (should NOT use ML)
    "call mom",
    "please call dad",
    "turn on flashlight",
    "switch on torch",
    "open camera",
    "open calculator",
    "send a message",
    "text my friend",
    "what is the weather today",
    "tell me the time",

    # ML / fallback
    "hi",
    "hello assistant",
    "do something random",
    "i am bored",

    "fuck u ",
    "maderchod",
    "benchode"
]

for t in tests:
    print("User:", t)
    print("Bot :", execute_action(t))
    print("-" * 40)
