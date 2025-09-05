# AI Resume Tailor

A full-stack AI-powered resume tailoring application built with **FastAPI**, **React + TypeScript**, **TailwindCSS**, and **Docker**.  
The app helps job seekers adapt their resumes to specific job descriptions, improving **ATS (Applicant Tracking System) scores** and highlighting missing keywords.

<img width="1042" height="961" alt="Screenshot from 2025-09-05 21-55-47" src="https://github.com/user-attachments/assets/9a41cabe-6724-4bd1-8c1c-3fdddee68ab4" />
---

## Features
- Upload your **resume (PDF/text)** and provide a **job description** + **target role**  
- Backend (FastAPI + OpenAI) analyzes and returns:
  - ATS score
  - Matched / missing keywords
  - Title & summary suggestions
  - Improved bullet points with rationale
  - Section-level changes
  - Tailored resume in Markdown format
- Frontend (React + TailwindCSS) for:
  - Uploading resumes & job descriptions
  - Viewing AI-generated recommendations
  - Reviewing side-by-side changes
- Dockerized with **Nginx proxy** for seamless frontend–backend integration

---

## Tech Stack
- **Frontend**: React, TypeScript, Vite, TailwindCSS, Axios, Nginx
- **Backend**: FastAPI, Python, Uvicorn, OpenAI API
- **Infrastructure**: Docker, Docker Compose

---

## Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/your-username/ai-resume-tailor.git
cd ai-resume-tailor
```

### 2. Configure environment variables
Create ```.env``` and fill in values:
```bash
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

### 3. Build & start with Docker Compose
```bash
docker compose up --build
```
- Frontend → http://localhost:5173
- Backend → http://localhost:8000/docs (Swagger UI)
