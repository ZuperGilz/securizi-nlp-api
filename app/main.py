from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Optional

from .nlp_engine import detect_allergens
from .classify_engine import classify_food

app = FastAPI(
    title="Securizi NLP API (Ringan)",
    description="Service kecil untuk deteksi alergi & klasifikasi menu MBG.",
)


class AnalyzeRequest(BaseModel):
    description: str = Field(..., description="Deskripsi menu, misal: 'Nasi, ayam goreng, sayur sop, susu UHT'")
    allergens: Optional[List[str]] = Field(
        default=None,
        description="Daftar alergi anak (misal: ['kacang','susu']). Kalau kosong, cek semua allergen default.",
    )


class AnalyzeResponse(BaseModel):
    description: str
    categories: List[str]
    detected_allergens: List[dict]
    danger: bool


@app.get("/")
def root():
    return {"message": "Securizi NLP API active"}


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze_menu(req: AnalyzeRequest):
    # klasifikasi makanan
    categories = classify_food(req.description)

    # deteksi alergi
    detected = detect_allergens(req.description, req.allergens or [])

    return AnalyzeResponse(
        description=req.description,
        categories=categories,
        detected_allergens=detected,
        danger=len(detected) > 0,
    )
