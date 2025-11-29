*KB Range Management System — FastAPI Backend*
Backend API for Kenya Bunduki Indoor Shooting Range (Production-Ready Architecture)

This repository contains the official backend service for the Kenya Bunduki Indoor Range Management System — built with FastAPI, Uvicorn, and a clean modular architecture designed for scalability, speed, and reliability.

Features (Current & Upcoming)
Implemented

FastAPI server with modular routing

Health & status endpoint (/status)

Clean project structure (app/main.py, routers/, models/, services/)

Ready for Docker deployment

Auto-reload development server

Planned Enhancements

Authentication (JWT-based login)

Client booking API

Range session scheduling & management

Armory inventory API (firearms, ammo, logs)

Digital Target Scoring Integration (Phase 2)

Training session management

Admin dashboard API endpoints

Project Architecture
app/
 ├── main.py            # Application entry point
 ├── routers/           # API endpoints / route handlers
 ├── models/            # Pydantic schemas
 └── services/          # Business logic layer


This modular design ensures:

Clean separation of concerns

Easy expansion (more APIs, more modules)

Maintainability and long-term scalability

▶️ How to Run Locally
1. Clone the repository
git clone https://github.com/UrbanusMasai/kb-range-management-system.git
cd kb-range-management-system

2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows

3. Install dependencies
pip install -r requirements.txt

4. Start the development server
uvicorn app.main:app --reload


The server will start at:
http://127.0.0.1:8000

Available Endpoints
Health Check
GET /

System Status
GET /status

Tech Stack

Python 3.10+

FastAPI (backend framework)

Uvicorn (ASGI server)

Pydantic (data validation)

Git & GitHub

VS Code

Author

Urbanus Masai Mutua
Backend Engineer | Range Manager | Firearms Systems Specialist

GitHub: https://github.com/UrbanusMasai

Portfolio: (coming soon)
Contact: +254790514995

License

This project will use MIT License 

Support the Project

If you find this useful, please star ⭐ the repo — it helps visibility and credibility.
