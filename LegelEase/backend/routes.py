from fastapi import APIRouter
from pydantic import BaseModel
from typing import Union, List, Optional

router = APIRouter()

class DocumentRequest(BaseModel):
    document_type: Optional[str] = "Legal Agreement"
    parties: Optional[Union[str, List[str]]] = ""
    terms: Optional[Union[str, List[str]]] = ""
    effective_date: Optional[str] = ""
    additional_instructions: Optional[str] = ""

@router.post("/generate")
@router.post("/api/generate")
def generate_doc(req: DocumentRequest):
    parties_str = "\n".join(req.parties) if isinstance(req.parties, list) else (req.parties or "")
    terms_str = "\n".join(req.terms) if isinstance(req.terms, list) else (req.terms or "")
    doc_type = req.document_type or "Legal Agreement"
    doc_text = f"LEGAL AGREEMENT\n\nThis {doc_type} is effective as of {req.effective_date}.\n\nPARTIES:\n{parties_str}\n\nTERMS:\n{terms_str}"

    return {"status": "success", "title": doc_type, "content": doc_text, "document": doc_text}