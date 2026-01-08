# in-app-contextual-assistant

An in-app, context-aware AI assistant that adapts its behavior based on the **current screen and user context**, rather than treating every command in isolation.

This project demonstrates how an assistant can behave differently for the *same user command* depending on where the user is inside an application.

---

## ✨ What Makes This Different

Most AI assistants only answer *what* the user asked.  
This assistant also understands **where** the user is.

Example:
- **Home screen**
  - User: `open profile`
  - Assistant: *Which profile do you want to open?*
- **Chat screen (with Riya)**
  - User: `open profile`
  - Assistant: *Opening Riya’s profile*

Same command. Different behavior.  
That difference is the entire point of this project.

---

## 🧠 Core Concepts Implemented

- **ML-based intent classification**
  - TF-IDF + Logistic Regression
- **Context-aware decision logic**
  - Screen-level and user-level context
- **Follow-up clarification flow**
  - Assistant remembers pending intent
- **In-app assistant UX**
  - Assistant runs as an overlay, not a separate app
- **Clean separation of concerns**
  - Intent detection ≠ Action execution ≠ UI

---

## 🏗 Architecture Overview
Android App (Kotlin)
│
│ user input + app context
▼
Flask Backend (Python)
│
├─ Intent Classifier (NLP / ML)
├─ Action Engine (context-aware logic)
└─ Reply Manager


- ML decides **what the user wants**
- Context decides **how the assistant should act**
- UI simply reflects the result

---

## 🧪 Example Flow

User: open profile
Context: chat_screen, selected_user=riya

→ Intent: open_profile
→ Context-aware action: open_current_chat_profile
→ Reply: Opening Riya’s profile


---

## 🛠 Tech Stack

**Backend**
- Python
- Flask
- scikit-learn
- NumPy / Pandas

**Client**
- Android
- Kotlin
- Bottom Sheet UI for in-app assistant

---

## 📁 Project Structure



AI/
├── actions/ # Action engine & context logic
├── nlp/ # Intent classifier & preprocessing
├── data/ # Intent datasets & replies
├── speech/ # Voice input (experimental)
├── app.py # Flask backend entry point
├── requirements.txt
└── README.md


---

## 🚀 Running the Backend


python app.py


Backend runs at:

http://localhost:5000

---

## 🧠 Training the Intent Model

python -m nlp.intent_classifier


Trained model files are intentionally not committed.
They can be regenerated at any time.
---
## 📌 Project Status


This is a prototype / portfolio project focused on:

system design

contextual reasoning

real-world assistant behavior

It is not a production-ready assistant and is intentionally kept simple to highlight architecture rather than scale.
---

## Demo
![
    
](<Screenshot 2026-01-08 221038.png>)

<video controls src="demo.mp4" title="Title"></video>


---
## 🔮 Future Improvements

Session-based context instead of in-memory state

Inline assistant responses inside chat UI

Voice-first assistant inside chat

Backend deployment (Render / Fly.io)

Context-aware suggestions
---

## 👤 Author

Anish Tiwari

If you’re reviewing this project:

The goal is not a smarter chatbot

The goal is a better assistant experience inside an app


---

