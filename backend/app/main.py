from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import tailor


app = FastAPI(title="AI Resume Tailor")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(tailor.router)


@app.get("/health")
async def health():
    return {"ok": True}