from speech.speech_engine import listen
from actions.action_engine import execute_action
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def run_assistant():
    speak("Assistant is running. Say something!")

    while True:
        text = listen()

        # STOP command
        if "stop" in text.lower() or "exit" in text.lower():
            speak("Stopping assistant. Goodbye!")
            break

        if text == "":
            speak("I didn't catch that. Please repeat.")
            continue

        result = execute_action(text)
        speak(result)

if __name__ == "__main__":
    run_assistant()
