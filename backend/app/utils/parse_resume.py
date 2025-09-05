from io import BytesIO
from typing import Tuple
import docx2txt
from pdfminer.high_level import extract_text


ALLOWED = {"pdf", "docx", "txt"}


def sniff_ext(filename: str) -> str:
    return filename.split(".")[-1].lower()


def parse_resume(file_bytes: bytes, filename: str) -> Tuple[str, str]:
    ext = sniff_ext(filename)
    if ext not in ALLOWED:
        raise ValueError("Unsupported file type. Use PDF/DOCX/TXT")
    if ext == "pdf":
        text = extract_text(BytesIO(file_bytes))
    elif ext == "docx":
        with BytesIO(file_bytes) as f:
            text = docx2txt.process(f)
    else:
        text = file_bytes.decode("utf-8", errors="ignore")
    return ext, text.strip()