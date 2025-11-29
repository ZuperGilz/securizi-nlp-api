from .food_dictionary import FOOD_INGREDIENTS
from .fuzzy_matcher import fuzzy_find

def extract_food_entities(ner_output):
    tokens = [x["word"].lower() for x in ner_output]
    return tokens

def detect_food(tokens):
    detected = []

    for t in tokens:
        for category, synonyms in FOOD_INGREDIENTS.items():
            for syn in synonyms:
                if syn in t:
                    detected.append((t, category))
    
    return detected

def detect_allergens(tokens, allergens):
    # cocokkan bahan yang ada dengan alergi anak
    matched = fuzzy_find(tokens, allergens)
    return matched
