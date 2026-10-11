# FNZ-Atom-
An AI-powered knowledge assistant built with FastAPI, LangGraph, and React that enables engineers to efficiently query business logic and automates test analysis workflows.
```markdown
# FNZ_ATOM – AI Business Design Backend

This project is a FastAPI-based backend that generates business designs, schemas, and SQL using AI.

## 1. Create Virtual Environment

From the project root directory, run:

### Windows
```bash
python -m venv venv
venv\Scripts\activate

```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate

```

After activation, you should see `(venv)` in your terminal.

## 2. Setup Environment Variables

This project uses environment variables for API keys. A template file is provided: `.env.test`

### Step 1: Create .env File

Copy `.env.test` and create a new file called `.env`:

```bash
copy .env.test .env        # Windows
cp .env.test .env          # macOS/Linux

```

### Step 2: Add Your API Key

Open `.env` and update the values.

Example:

```env
GEMINI_API_KEY=your_api_key_here

```

Make sure the file is saved.

## 3. Install Dependencies

Install all required packages using:

```bash
pip install -r requirements.txt

```

Wait until installation completes.

## 4. Run the Server

From the project root, start the FastAPI server:

```bash
python -m uvicorn app.main:app --reload
# Or depending on your python version/port preferences
python3.10 -m uvicorn app.main:app --reload --port 8080

```

If successful, you will see:
`Uvicorn running on http://127.0.0.1:8000`

## 5. Test Using Postman (WebSocket)

This project uses WebSocket for chat communication.

### WebSocket Endpoint

`ws://127.0.0.1:8000/ws/chat`

### Using Postman

1. Open Postman
2. Click **New**
3. Select **WebSocket Request**
4. Enter the URL: `ws://127.0.0.1:8000/ws/chat`
5. Click **Connect**
6. Send messages in JSON or text format

Example:

```json
{
  "message": "Design a complaint tracking system"
}

```

## 6. API Documentation (Optional)

FastAPI provides automatic API documentation. After starting the server, open:

`http://127.0.0.1:8000/docs`

## Project Structure (Simplified)

```text
FNZ_ATOM/
├── app/
│   ├── main.py
│   ├── api/
│   └── services/
├── venv/
├── .env
├── .env.test
├── requirements.txt
└── README.md

```

## Notes

* Always activate the virtual environment before running the server
* Never commit `.env` files to public repositories
* Update `requirements.txt` when new packages are added

## Quick Start Summary

```bash
python -m venv venv
venv\Scripts\activate
copy .env.test .env
pip install -r requirements.txt
python -m uvicorn app.main:app --reload

```

Then connect using Postman:
`ws://127.0.0.1:8000/ws/chat`

```

```
