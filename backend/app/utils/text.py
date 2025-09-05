import re
from typing import List

STOPWORDS = set("""a an the and or but if then while to for of in on with as by at from into over under between out up down not""".split())


def extract_keywords(text: str, top_k: int = 60) -> List[str]:
    tokens = re.findall(r"[A-Za-z][A-Za-z+.#/0-9-]*", text.lower())
    freq = {}
    for t in tokens:
        if t in STOPWORDS or len(t) < 2:
            continue
        freq[t] = freq.get(t, 0) + 1
    return [w for w, _ in sorted(freq.items(), key=lambda x: x[1], reverse=True)[:top_k]]


def compute_score(jd_keywords: List[str], resume_text: str) -> (int, List[str], List[str]):
    resume_low = resume_text.lower()
    matched = []
    missing = []
    for kw in jd_keywords:
        pattern = r"\b" + re.escape(kw.lower()) + r"\b"
        if re.search(pattern, resume_low):
            matched.append(kw)
        else:
            missing.append(kw)
    if jd_keywords:
        score = int(100 * len(matched) / max(10, len(jd_keywords)))
    else:
        score = 50
    return score, matched, missing