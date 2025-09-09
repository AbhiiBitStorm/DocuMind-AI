from celery import Celery
from ocr_module import extract_text_from_image
from nlp_module import get_entities, get_highlighted_text
from text_module import summarize_text, translate_text
import time

celery = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

@celery.task
def process_document_task(filepath, language):
    """Background task to run the full AI pipeline."""
    text = extract_text_from_image(filepath)
    if not text or len(text.strip()) < 20:
        return {'error': 'Could not extract sufficient text. Please use a clearer image.'}

    summary = summarize_text(text)
    translation = translate_text(summary, language)
    entities = get_entities(text)
    highlighted_text = get_highlighted_text(text)
    
    return {
        'summary': summary,
        'translation': translation,
        'entities': entities,
        'highlighted_text': highlighted_text
    }