# utils/skills.py

COMMON_SKILLS = [
    "python","java","c++","sql","excel","power bi","tableau","machine learning",
    "deep learning","nlp","aws","azure","gcp","docker","kubernetes","pandas",
    "numpy","scikit-learn","tensorflow","pytorch","fastapi","streamlit",
    "data analysis","data science","statistics","git","github","linux"
]

def extract_skills(text: str):
    text_lower = text.lower()

    found = []
    for skill in COMMON_SKILLS:
        if skill in text_lower:
            found.append(skill)

    return sorted(list(set(found)))