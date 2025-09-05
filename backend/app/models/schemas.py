from pydantic import BaseModel, Field
from typing import List, Optional


class TailorRequest(BaseModel):
    job_description: str
    resume_text: str
    target_role: Optional[str] = None


class ChangeItem(BaseModel):
    section: str
    before: str
    after: str


class Suggestion(BaseModel):
    text: str
    rationale: str
    mapped_requirement: Optional[str] = None


class TailorResponse(BaseModel):
    score: int = Field(ge=0, le=100)
    matched_keywords: List[str]
    missing_keywords: List[str]
    title_suggestion: Optional[str] = None
    summary_suggestion: Optional[str] = None
    bullet_suggestions: List[Suggestion]
    changes: List[ChangeItem]
    tailored_resume_markdown: Optional[str] = None