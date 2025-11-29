from rapidfuzz import fuzz

def fuzzy_find(ingredients: list[str], allergen_list: list[str]):
    matched = []

    for ing in ingredients:
        for al in allergen_list:
            score = fuzz.partial_ratio(ing.lower(), al.lower())
            if score >= 80:  # ambang aman
                matched.append((ing, al, score))
    
    return matched
