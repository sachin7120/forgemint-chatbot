# ForgeMint Chatbot

A lightweight customer-support chatbot for **ForgeMint**. The project uses a FastAPI backend and a plain HTML, CSS, and JavaScript frontend. It answers common questions about ForgeMint’s services and offers a WhatsApp handoff when a visitor needs pricing or a real person.

## Features

- FastAPI JSON API with CORS enabled for the frontend
- Rule-based answers for greetings, company information, services, process, contact, and more
- ForgeMint knowledge stored in one editable Python dictionary
- WhatsApp handoff for pricing, sales, contact, new-project, and fallback questions
- Health-check endpoint for deployment monitoring
- Responsive static frontend

## Project structure

```text
forgemint-chatbot/
├── backend/
│   ├── main.py            # FastAPI API routes and request/response models
│   ├── chatbot.py         # Intent matching and chatbot replies
│   ├── knowledge.py       # ForgeMint company details, services, and contact data
│   ├── requirements.txt   # Python dependencies
│   └── __pycache__/       # Generated Python cache; do not edit or commit
├── frontend/
│   ├── index.html         # Chat page
│   ├── script.js          # Calls the FastAPI API and renders replies
│   └── style.css          # Frontend styles
├── .gitattributes
└── README.md
```

## Requirements

- Python 3.10 or newer
- pip
- A modern web browser

## Setup

Open PowerShell in the repository folder:

```powershell
cd C:\Users\Intern\Documents\GitHub\forgemint-chatbot
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r .\backend\requirements.txt
```

If the `py` command is unavailable, install Python from [python.org](https://www.python.org/downloads/) and ensure it is added to your system PATH.

## Run the backend

From the repository root, run:

```powershell
uvicorn backend.main:app --reload
```

Or run it from the backend directory:

```powershell
cd backend
uvicorn main:app --reload
```

The API starts at http://127.0.0.1:8000.

| URL | Purpose |
|---|---|
| http://127.0.0.1:8000/ | API welcome response |
| http://127.0.0.1:8000/health | Health check |
| http://127.0.0.1:8000/docs | Interactive FastAPI documentation |

## Run the frontend

With the backend running, open [frontend/index.html](frontend/index.html) in a browser. If `script.js` uses a relative `/chat` URL, serve the frontend from the same origin or update its API base URL to `http://127.0.0.1:8000`.

For a local static server, from the repository root run:

```powershell
py -m http.server 5500 --directory frontend
```

Then open http://127.0.0.1:5500. The backend already allows cross-origin browser requests during development.

## API

### `GET /`

Returns a simple confirmation that the API is running.

```json
{
  "message": "ForgeMint Chatbot API is running"
}
```

### `GET /health`

Returns:

```json
{
  "status": "ok"
}
```

### `POST /chat`

Send a visitor message:

```json
{
  "message": "What services does ForgeMint offer?"
}
```

The response includes:

```json
{
  "reply": "…",
  "show_agent": false,
  "whatsapp_url": null
}
```

`show_agent` tells the frontend whether it should show a “talk to an agent” action. `whatsapp_url` is supplied when the bot should direct the visitor to WhatsApp.

## Current chatbot topics

The bot currently recognizes questions about:

- Greetings and thank-you messages
- What ForgeMint is and where it is located
- Services and solutions
- Website and web development
- Mobile app development
- E-commerce solutions
- Custom CRM and ERP systems
- UI/UX design
- Pricing and quotations
- Development process
- Maintenance and post-launch support
- Contact details, Instagram, and starting a project

Pricing, contact, new-project, and unknown questions are handed off to WhatsApp so a real team member can respond.

## Update ForgeMint content

Edit [backend/knowledge.py](backend/knowledge.py) to change approved public information:

- Company name, description, website, and location
- Service list
- Development process
- Engagement options
- Email, phone, WhatsApp number, and social links

The WhatsApp number must use international digits only—no `+`, spaces, or hyphens. For example:

```python
"whatsapp": "918556868095"
```

Edit [backend/chatbot.py](backend/chatbot.py) to add an intent. Add related keywords and return a reply dictionary in the same format:

```python
return {
    "reply": "Your approved answer.",
    "show_agent": False,
    "whatsapp_url": None
}
```

For a human handoff, use:

```python
return {
    "reply": "A team member can help with that.",
    "show_agent": True,
    "whatsapp_url": create_whatsapp_url()
}
```

## Content and security rules

Only add verified, ForgeMint-approved content to `knowledge.py`. Do not include:

- API keys, passwords, access tokens, or database credentials
- Client names, private project details, proposals, or contracts
- Payment or banking data
- Pricing or delivery promises that have not been approved

The current `allow_origins=["*"]` CORS setting is convenient for local development. Before production, restrict it to your real frontend domain, for example `https://forgemint.in`.

## Recommended next improvements

- Move the `FORGEMINT_KNOWLEDGE` dictionary into a versioned JSON file.
- Add unit tests for the main intents and WhatsApp handoff.
- Add input length limits and rate limiting to `/chat`.
- Store leads in a secured database only after consent.
- Add semantic search or an AI model for questions that do not match keywords.
- Add logging and error monitoring before deployment.

## License

Add a license file before sharing or distributing this project publicly.
