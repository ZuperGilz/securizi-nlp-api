from fuzzywuzzy import fuzz

def normalize_text(text: str) -> str:
    return " ".join(text.lower().strip().split())


def fuzzy_contains(text: str, keyword: str, threshold: int = 80) -> bool:
    """
    Cek apakah text "mirip" dengan keyword (misal 'kacang mete' vs 'kacang')
    threshold 0-100, makin tinggi makin ketat.
    """
    return fuzz.partial_ratio(text.lower(), keyword.lower()) >= threshold
