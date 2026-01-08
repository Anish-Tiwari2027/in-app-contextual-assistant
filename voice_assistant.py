from speech.speech_engine import listen
from actions.action_engine import execute_action

print("AI Assistant is running... Say something! (say 'stop' to exit)")

while True:
    text = listen()

    if text == "":
        print("Didn't understand, try again.")
        continue

    # STOP condition
    if "stop" in text.lower() or "exit" in text.lower() or "quit" in text.lower():
        print("Assistant: Stopping. Goodbye!")
        break

    result = execute_action(text)
    print("Assistant:", result)
