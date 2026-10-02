# 🎙️ AI Voice Lead Agent

An AI-powered voice-based lead qualification system that collects loan-related information through a natural voice conversation and evaluates the lead using a FastAPI backend.

The project combines **Vapi**, **FastAPI**, **Python**, and **ngrok** to create an end-to-end voice-to-backend workflow.

---

## 📌 Project Overview

The **AI Voice Lead Agent** automates the initial stage of loan lead qualification.

Instead of manually collecting basic customer information, the voice agent interacts with the user, collects:

* Monthly income
* Requested loan amount

The collected information is sent to a backend API, where predefined business rules are applied to determine whether the lead qualifies for the next stage.

### Current Qualification Rule

A lead is considered qualified when:

```text
Monthly Income >= ₹50,000
AND
Loan Amount <= ₹10,00,000
```

The backend returns one of two outcomes:

```text
qualified_for_next_step
```

or

```text
needs_review
```

> **Note:** This is a prototype demonstrating voice-based lead qualification and is not intended to make real-world lending decisions.

---

# 🏗️ System Architecture

```text
                    ┌──────────────────┐
                    │      User        │
                    │  Voice Conversation
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   Vapi Voice     │
                    │      Agent       │
                    └────────┬─────────┘
                             │
                             │ check_lead()
                             ▼
                    ┌──────────────────┐
                    │   ngrok HTTPS    │
                    │      Tunnel      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  FastAPI Backend │
                    │    /check-lead   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Qualification    │
                    │     Logic        │
                    └────────┬─────────┘
                             │
                             ▼
              ┌──────────────────────────────┐
              │        Lead Result           │
              │                              │
              │ qualified_for_next_step     │
              │            OR                │
              │ needs_review                 │
              └──────────────┬───────────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   Vapi Agent     │
                    │ Voice Response   │
                    └──────────────────┘
```

### Workflow

1. The user speaks with the Vapi voice agent.
2. The agent collects the required loan information.
3. Vapi calls the `check_lead` backend function.
4. ngrok securely exposes the local FastAPI server through HTTPS.
5. FastAPI receives the request.
6. The qualification logic evaluates the lead.
7. The backend returns the qualification result.
8. Vapi uses the result to continue the conversation.

---

# 🛠️ Tech Stack

| Technology   | Purpose                                  |
| ------------ | ---------------------------------------- |
| **Python**   | Backend programming                      |
| **FastAPI**  | REST API development                     |
| **Vapi**     | AI voice agent and conversation handling |
| **ngrok**    | HTTPS tunnel for local backend           |
| **REST API** | Communication between Vapi and backend   |
| **Uvicorn**  | FastAPI development server               |
| **Git**      | Version control                          |
| **GitHub**   | Source code and project hosting          |

---

# 📂 Project Structure

```text
AI-Voice-Lead-Agent/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── screenshots/
│   ├── vapi-agent.png
│   ├── vapi-check-lead-tool.png
│   ├── fastapi-backend.png
│   ├── api-test.png
│   └── voice-agent-test.png
│
├── docs/
│   └── architecture.png
│
└── venv/              # Local only - not uploaded to GitHub
```

---

# 🔌 Backend API

The FastAPI backend provides the following endpoint:

```text
POST /check-lead
```

### Example Request

```json
{
    "monthly_income": 60000,
    "loan_amount": 500000
}
```

### Example Response

```json
{
    "status": "qualified_for_next_step",
    "monthly_income": 60000,
    "loan_amount": 500000
}
```

For a lead that does not satisfy the conditions:

```json
{
    "status": "needs_review",
    "monthly_income": 40000,
    "loan_amount": 1200000
}
```

---

# ⚙️ How to Run the Project

## 1. Clone the Repository

```bash
git clone https://github.com/rsouparnika/AI_Voice_Lead_Agent.git
```

Move into the project directory:

```bash
cd AI_Voice_Lead_Agent
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate the Virtual Environment

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

You should see:

```text
(venv)
```

at the beginning of your terminal prompt.

---

## 4. Install Dependencies

```powershell
pip install -r requirements.txt
```

---

# 🚀 Start the FastAPI Backend

Run:

```powershell
uvicorn main:app --reload
```

The backend will start at:

```text
http://localhost:8000
```

You can verify that it is running by opening:

```text
http://localhost:8000
```

Expected response:

```json
{
    "message": "AI Voice Lead Agent backend is running!"
}
```

---

# 🧪 Test the API

Open another PowerShell terminal while the FastAPI server is running.

Activate the environment if required:

```powershell
cd "C:\Users\Souparnika R\Downloads\AI-Voice-Lead-Agent"
.\venv\Scripts\Activate.ps1
```

Send a test request:

```powershell
$body = @{
    monthly_income = 60000
    loan_amount = 500000
} | ConvertTo-Json

Invoke-RestMethod `
    -Uri "http://localhost:8000/check-lead" `
    -Method Post `
    -ContentType "application/json" `
    -Body $body
```

Expected result:

```text
status                  monthly_income loan_amount
------                  -------------- -----------
qualified_for_next_step          60000      500000
```

---

# 🌐 Connect the Backend to Vapi

Because the FastAPI server is running locally, Vapi cannot directly access:

```text
http://localhost:8000
```

ngrok is used to expose the local server through a public HTTPS URL.

## 1. Start ngrok

Keep FastAPI running and open another terminal.

Run:

```powershell
ngrok http 8000
```

ngrok will provide an HTTPS forwarding URL similar to:

```text
https://example-name.ngrok-free.dev
```

---

## 2. Configure the Vapi Tool

In Vapi, create/configure the `check_lead` function.

The tool accepts:

```text
monthly_income
loan_amount
```

Set the tool's server endpoint to:

```text
https://YOUR-NGROK-URL/check-lead
```

Replace `YOUR-NGROK-URL` with the HTTPS URL generated by your ngrok session.

> **Important:** The ngrok URL can change when you restart ngrok unless you use a reserved/static domain.

---

# 🎙️ Run the Complete Voice Workflow

For a complete test, run the following components:

### Terminal 1 — FastAPI

```powershell
uvicorn main:app --reload
```

### Terminal 2 — ngrok

```powershell
ngrok http 8000
```

### Vapi

Make sure the `check_lead` tool uses the current ngrok HTTPS endpoint.

Then start the Vapi voice agent and provide example information such as:

```text
Monthly income: ₹60,000
Loan amount: ₹5,00,000
```

The flow becomes:

```text
User speaks
     ↓
Vapi Voice Agent
     ↓
check_lead()
     ↓
ngrok
     ↓
FastAPI
     ↓
Qualification Logic
     ↓
Result
     ↓
Vapi Voice Response
```

---

# 📸 Screenshots

### Vapi Voice Agent

![Vapi Agent](screenshots/vapi-agent.png)

### Vapi `check_lead` Tool

![Vapi Check Lead Tool](screenshots/vapi-check-lead-tool.png)

### FastAPI Backend

![FastAPI Backend](screenshots/fastapi-backend.png)

### API Test

![API Test](screenshots/api-test.png)

### Voice Agent Test

![Voice Agent Test](screenshots/voice-agent-test.png)

---

# 🔐 Security

Do not commit sensitive information such as:

* API keys
* Authentication tokens
* Passwords
* `.env` files
* Private credentials

The project `.gitignore` excludes environment files and the local virtual environment.

---

# 🔮 Future Improvements

Possible future extensions include:

* Lead database integration
* Persistent conversation history
* Advanced lead scoring
* CRM integration
* Automated lead follow-up
* Lead analytics dashboard
* Power BI integration
* Multilingual voice interaction
* Cloud deployment
* Authentication and API security
* More sophisticated qualification rules

---
