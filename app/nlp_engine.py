from typing import List, Dict
from .allergen_keywords import ALLERGEN_SYNONYMS
from .rule_patterns import RULE_PATTERNS
from .utils import normalize_text, fuzzy_contains


def _get_synonyms_for_user(allergens: List[str]) -> Dict[str, List[str]]:
    """
    Dari list alergi anak (misal: ['kacang', 'susu']),
    ambil hanya sinonim yang relevan.
    Kalau list kosong -> pakai semua allergen default.
    """
    if not allergens:
        return ALLERGEN_SYNONYMS

    result: Dict[str, List[str]] = {}
    lower_allergens = [a.lower().strip() for a in allergens]

    for base, syns in ALLERGEN_SYNONYMS.items():
        if base in lower_allergens:
            result[base] = syns
    return result


def detect_allergens(description: str, user_allergens: List[str] | None = None) -> List[Dict]:
    """
    Deteksi alergi berdasarkan deskripsi menu + daftar alergi anak.
    Return list dict: [{base, found, via_rule}, ...]
    """
    text = normalize_text(description)
    synonyms_map = _get_synonyms_for_user(user_allergens or [])

    detected: List[Dict] = []

    for base, synonyms in synonyms_map.items():
        base_found = False
        found_word = None
        via_rule = False

        # 1) cek langsung keyword / fuzzy
        for syn in synonyms:
            if syn in text or fuzzy_contains(text, syn):
                base_found = True
                found_word = syn
                break

        # 2) kalau belum ketemu, cek pola kalimat (rule-based)
        if not base_found:
            for syn in synonyms:
                for pattern in RULE_PATTERNS:
                    phrase = pattern.format(syn)
                    if phrase in text or fuzzy_contains(text, phrase):
                        base_found = True
                        found_word = syn
                        via_rule = True
                        break
                if base_found:
                    break

        if base_found and found_word:
            detected.append(
                {
                    "allergen": base,      # misal: 'kacang'
                    "matched_word": found_word,
                    "via_rule": via_rule,
                }
            )

    return detected
