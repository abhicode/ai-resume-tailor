from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from ..utils.parse_resume import parse_resume
from ..utils.text import extract_keywords, compute_score
from ..models.schemas import TailorRequest, TailorResponse
from ..services.llm import tailor_with_llm
import json

router = APIRouter(prefix="/api", tags=["tailor"])

@router.post("/ingest", response_model=TailorRequest)
async def ingest_resume(job_description: str = Form(...), file: UploadFile = File(...), target_role: str = Form(None)):
    content = await file.read()
    try:
        _, resume_text = parse_resume(content, file.filename)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return TailorRequest(job_description=job_description, resume_text=resume_text, target_role=target_role)


@router.post("/tailor", response_model=TailorResponse)
async def tailor(req: TailorRequest):
    jd_keywords = extract_keywords(req.job_description, top_k=50)
    score, matched, missing = compute_score(jd_keywords, req.resume_text)

    llm_json = tailor_with_llm({
        "job_description": req.job_description,
        "resume_text": req.resume_text,
        "target_role": req.target_role,
        })
    if isinstance(llm_json, str):
        try:
            llm_json = json.loads(llm_json)
        except Exception:
            llm_json = {}

    return TailorResponse(
        score=llm_json.get("score", score),
        matched_keywords=llm_json.get("matched_keywords", matched),
        missing_keywords=llm_json.get("missing_keywords", missing),
        title_suggestion=llm_json.get("title_suggestion"),
        summary_suggestion=llm_json.get("summary_suggestion"),
        bullet_suggestions=llm_json.get("bullet_suggestions", []),
        changes=llm_json.get("changes", []),
        tailored_resume_markdown=llm_json.get("tailored_resume_markdown"),
    )