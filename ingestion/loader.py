from pypdf import PdfReader
from ingestion.ocr import deepseek_ocr

def load_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted
        else:
            text += deepseek_ocr(file_path)

    return text

#for Streamlit / external entry points
def load_document(file_path: str) -> str:
    return load_pdf(file_path)
