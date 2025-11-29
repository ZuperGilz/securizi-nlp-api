from typing import List
from .allergen_keywords import FOOD_CATEGORIES
from .utils import normalize_text


def classify_food(description: str) -> List[str]:
    """
    Klasifikasi kasar menu ke kategori (protein, karbohidrat, sayur, dll)
    berdasarkan keyword sederhana.
    """
    text = normalize_text(description)
    found_categories: List[str] = []

    for category, keywords in FOOD_CATEGORIES.items():
        for k in keywords:
            if k in text:
                found_categories.append(category)
                break

    # hilangkan duplikasi
    return sorted(list(set(found_categories)))
