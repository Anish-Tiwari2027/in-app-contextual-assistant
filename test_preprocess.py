from nlp.preprocess import preprocess_text

# Sample sentences to test
tests = [
    "Please open the camera!",
    "CALL my MOM",
    "Send a message to Riya saying I reached",
    "Turn ON the flashlight please",
    "What's the weather today?",
    "can u call niharika plzz"
]

for text in tests:
    print("Original:", text)
    print("Processed:", preprocess_text(text))
    print()
