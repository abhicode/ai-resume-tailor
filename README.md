# AI Resume Tailor ✨

A full-stack AI-powered resume tailoring application built with **FastAPI**, **React + TypeScript**, **TailwindCSS**, and **Docker**.  
The app helps job seekers adapt their resumes to specific job descriptions, improving **ATS (Applicant Tracking System) scores** and highlighting missing keywords.

---

## 🚀 Features
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

## 🛠️ Tech Stack
- **Frontend**: React, TypeScript, Vite, TailwindCSS, Axios, Nginx
- **Backend**: FastAPI, Python, Uvicorn, OpenAI API
- **Infrastructure**: Docker, Docker Compose

---

## 📦 Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/your-username/ai-resume-tailor.git
cd ai-resume-tailor