import spacy

# تحميل النموذج الإنجليزي الصغير
nlp = spacy.load("en_core_web_sm")

# جملة اختبار
text = "Saeed is a pharmacy student who wants to become an AI engineer."

# تحليل الجملة
doc = nlp(text)

# طباعة التوكينات والوسوم النحوية
for token in doc:
    print(f"{token.text:<12} -> {token.pos_:<10} ({token.dep_})")
    