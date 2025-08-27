import spacy

nlp = spacy.load("pt_core_news_sm")

def clean_text(text):
    doc = nlp(text)
    tokens = [
        token.lemma_.lower() for token in doc
        if not token.is_stop and not token.is_punct
    ]
    return " ".join(tokens)