import spacy
from functools import lru_cache

nlp = spacy.load("en_core_web_sm")

@lru_cache(maxsize=128)
def get_entities(text):
    doc = nlp(text)
    return [{'text': ent.text, 'label': ent.label_} for ent in doc.ents]

@lru_cache(maxsize=128)
def get_highlighted_text(text):
    doc = nlp(text)
    highlighted_html = ""
    last_end = 0
    for ent in doc.ents:
        start, end, label = ent.start_char, ent.end_char, ent.label_
        highlighted_html += text[last_end:start]
        highlighted_html += f'<mark class="entity {label}">{ent.text}<span class="entity-label">{label}</span></mark>'
        last_end = end
    highlighted_html += text[last_end:]
    return highlighted_html