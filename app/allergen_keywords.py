# Daftar allergen dan sinonim / variasi penulisannya
# Kamu bisa bebas nambahin sesuai kebutuhan sekolah

ALLERGEN_SYNONYMS: dict[str, list[str]] = {
    "kacang": [
        "kacang",
        "kacang tanah",
        "kacang mete",
        "kacang mede",
        "kacang mete",
        "groundnut",
        "peanut",
        "kacang2an",
        "kacang-kacangan",
    ],
    "susu": [
        "susu",
        "susu sapi",
        "susu uht",
        "uht",
        "milk",
        "dairy",
        "keju",
        "cheese",
        "yogurt",
        "yoghurt",
        "laktosa",
        "lactose",
    ],
    "udang": [
        "udang",
        "udang goreng",
        "udang rebus",
        "ebi",
        "ebi furai",
        "shrimp",
        "prawn",
    ],
    "telur": [
        "telur",
        "telur ayam",
        "telur rebus",
        "telur dadar",
        "egg",
        "omelet",
        "omelette",
    ],
    "ikan": [
        "ikan",
        "ikan goreng",
        "ikan bakar",
        "fish",
        "tuna",
        "salmon",
        "tongkol",
        "teri",
    ],
    "seafood": [
        "seafood",
        "cumi",
        "cumi-cumi",
        "sotong",
        "kerang",
        "kepiting",
        "crab",
        "clam",
        "oyster",
    ],
}

# kategori bahan makan umum (untuk klasifikasi kasar)
FOOD_CATEGORIES: dict[str, list[str]] = {
    "protein": ["ayam", "telur", "ikan", "daging", "sapi", "udang", "tahu", "tempe"],
    "karbohidrat": ["nasi", "roti", "mie", "spaghetti", "kentang", "ubi"],
    "sayur": ["sayur", "bayam", "sop", "wortel", "brokoli", "kangkung", "kol"],
    "buah": ["apel", "pisang", "mangga", "pepaya", "jeruk", "buah"],
    "minuman": ["susu", "teh", "kopi", "jus", "sirup", "squash"],
    "snack": ["biskuit", "keripik", "kue", "roti", "snack", "camilan"],
}
