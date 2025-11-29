from fastapi import APIRouter
from pydantic import BaseModel
from app.models.indo_bert import IndoBertNER
from app.utils.ner_parser import extract_food_entities, detect_food, detect_allergens

router = APIRouter()
ner_model = IndoBertNER()

class InputData(BaseModel):
    menu: str
    allergens: list[str]

@router.post("/analyze-menu")
async def analyze_menu(data: InputData):
    ner_result = ner_model.extract(data.menu)

    tokens = extract_food_entities(ner_result)
    detected_food = detect_food(tokens)
    matched_allergens = detect_allergens(tokens, data.allergens)

    return {
        "tokens": tokens,
        "detected_food": detected_food,
        "matched_allergens": matched_allergens,
        "danger": len(matched_allergens) > 0
    }
