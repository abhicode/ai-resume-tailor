import os
from typing import Dict
from openai import OpenAI


MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


SYSTEM_PROMPT = (
    "You are an expert resume coach and ATS consultant. For a given resume and job description, "
    "return a JSON object strictly matching the TailorResponse schema. Keep changes specific, "
    "concise, and measurable. Map suggestions to JD requirements."
)


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def tailor_with_llm(payload: Dict) -> Dict:
    jd = payload["job_description"]
    resume = payload["resume_text"]
    target_role = payload.get("target_role")


    user_prompt = f"""
        Job Description:\n{jd}\n\nResume:\n{resume}\n\nTarget Role: {target_role or "(not specified)"}


        Return JSON with keys: score, matched_keywords, missing_keywords, title_suggestion, summary_suggestion, bullet_suggestions (each with text, rationale, mapped_requirement), changes (each with section, before, after), tailored_resume_markdown. Ensure valid JSON.
        """


    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.2,
        response_format={"type": "json_object"},
    )
    return resp.choices[0].message.parsed if hasattr(resp.choices[0].message, 'parsed') else resp.choices[0].message.content