from transformers import pipeline
import torch
from functools import lru_cache

# A simple cache for pipeline objects
_PIPELINE_CACHE = {}

def _get_pipeline(task, model):
    if model in _PIPELINE_CACHE:
        return _PIPELINE_CACHE[model]
    
    device = 0 if torch.cuda.is_available() else -1
    pipe = pipeline(task, model=model, device=device)
    _PIPELINE_CACHE[model] = pipe
    return pipe

@lru_cache(maxsize=128)
def summarize_text(text):
    if len(text.split()) < 40:
        return text
    summarizer = _get_pipeline("summarization", model="t5-small")
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']

@lru_cache(maxsize=128)
def translate_text(text, target_language='hi'):
    model_map = {
        'hi': "Helsinki-NLP/opus-mt-en-hi", 'mr': "Helsinki-NLP/opus-mt-en-mr",
        'bn': "Helsinki-NLP/opus-mt-en-bn", 'es': "Helsinki-NLP/opus-mt-en-es",
    }
    model_name = model_map.get(target_language, model_map['hi'])
    translator = _get_pipeline("translation", model=model_name)
    translation = translator(text)
    return translation[0]['translation_text']