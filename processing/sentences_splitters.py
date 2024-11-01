import nltk
import re
import spacy
import stanza
from trankit import Pipeline
from sentence_splitter import SentenceSplitter
from blingfire import *
import pysbd
from mosestokenizer import MosesPunctuationNormalizer


def file_normalization(raw_data):
    normalized_data = []
    with MosesPunctuationNormalizer('fr') as normalize:
        for sentence in raw_data:
            normalized_data.append(normalize(sentence).strip())
    return ' '.join(normalized_data)


def regex_splitter(filepath):
    alphabets = "([A-Za-z])"
    prefixes = "(Mr|St|Mrs|Ms|Dr|M)[.]"
    suffixes = "(Inc|Ltd|Jr|Sr|Co)"
    starters = "(Mr|Mrs|Ms|Dr|M|Mme\s|Il\s|Ils\s|Elle\s|Elles\s)"
    acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
    websites = "[.](com|net|org|io|gov)"
    digits = "([0-9])"
    text = " " + file_normalization(filepath) + "  "
    text = text.replace("\n", " ")
    text = re.sub(prefixes, "\\1<prd>", text)
    text = re.sub(websites, "<prd>\\1", text)
    text = re.sub(digits + "[.]" + digits, "\\1<prd>\\2", text)
    if "..." in text:
        text = text.replace("...", "<prd><prd><prd>")
    if "Ph.D" in text:
        text = text.replace("Ph.D.", "Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] ", " \\1<prd> ", text)
    text = re.sub(acronyms + " " + starters, "\\1<stop> \\2", text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]", "\\1<prd>\\2<prd>\\3<prd>", text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]", "\\1<prd>\\2<prd>", text)
    text = re.sub(" " + suffixes + "[.] " + starters, " \\1<stop> \\2", text)
    text = re.sub(" " + suffixes + "[.]", " \\1<prd>", text)
    text = re.sub(" " + alphabets + "[.]", " \\1<prd>", text)
    if "”" in text:
        text = text.replace(".”", "”.")
    if "\"" in text:
        text = text.replace(".\"", "\".")
    if "!" in text:
        text = text.replace("!\"", "\"!")
    if "?" in text:
        text = text.replace("?\"", "\"?")
    text = text.replace(".", ".<stop>")
    text = text.replace("?", "?<stop>")
    text = text.replace("!", "!<stop>")
    text = text.replace("<prd>", ".")
    text = text.split("<stop>")
    result = text[:-1]
    return [token.strip() for token in result]


def nltk_splitter(filepath):
    result = nltk.tokenize.sent_tokenize(file_normalization(filepath), "french")
    return result


def spacy_splitter(filepath):
    nlp = spacy.load('fr_dep_news_trf')
    result = nlp(file_normalization(filepath))
    return [r.text for r in result.sents]


def koehn_splitter(filepath):
    splitter = SentenceSplitter(language='fr')
    result = splitter.split(text=file_normalization(filepath))
    return result


def stanford_splitter(filepath):
    pipeline = stanza.Pipeline(lang='wo', processors='tokenize')  # lang='wo' also available for wolof
    result = pipeline(file_normalization(filepath))
    return [token.text for token in result.sentences]


def trankit_splitter(filepath):
    pipeline = Pipeline(lang='french', embedding='xlm-roberta-large',
                        cache_dir='../venv/lib/python3.8/site-packages/trankit/cache')
    result = pipeline.ssplit(file_normalization(filepath))
    return [token['text'] for token in result['sentences']]


def blingfire_splitter(filepath):
    return text_to_sentences(file_normalization(filepath))


def pysbd_splitter(filepath):
    segmenter = pysbd.Segmenter(language='fr', clean=False)
    return segmenter.segment(file_normalization(filepath))
