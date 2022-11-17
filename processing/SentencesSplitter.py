# -*- coding: utf-8 -*-

import nltk
import re
import spacy
import stanza
from trankit import Pipeline
from sentence_splitter import SentenceSplitter
from mosestokenizer import MosesPunctuationNormalizer


def file_reading(filepath):
    with open(filepath, encoding='utf-8') as f:
        raw_data = f.readlines()
    cleaned_data = []
    for line in raw_data:
        cleaned_data.append(line.strip())
    with MosesPunctuationNormalizer('fr') as normalize:
        cleaned_data = normalize(' '.join(cleaned_data))
    return cleaned_data


def regex_splitter(filepath):
    alphabets = "([A-Za-z])"
    prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
    suffixes = "(Inc|Ltd|Jr|Sr|Co)"
    starters = "(Mr|Mrs|Ms|Dr|Mme\s|Il\s|Ils\s|Elle\s|Elles\s)"
    acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
    websites = "[.](com|net|org|io|gov)"
    digits = "([0-9])"

    text = " " + file_reading(filepath) + "  "
    text = text.replace("\n", " ")
    text = re.sub(prefixes, "\\1<prd>", text)
    text = re.sub(websites, "<prd>\\1", text)
    text = re.sub(digits + "[.]" + digits, "\\1<prd>\\2", text)
    if "..." in text: text = text.replace("...", "<prd><prd><prd>")
    if "Ph.D" in text: text = text.replace("Ph.D.", "Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] ", " \\1<prd> ", text)
    text = re.sub(acronyms + " " + starters, "\\1<stop> \\2", text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]", "\\1<prd>\\2<prd>\\3<prd>", text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]", "\\1<prd>\\2<prd>", text)
    text = re.sub(" " + suffixes + "[.] " + starters, " \\1<stop> \\2", text)
    text = re.sub(" " + suffixes + "[.]", " \\1<prd>", text)
    text = re.sub(" " + alphabets + "[.]", " \\1<prd>", text)
    if "”" in text: text = text.replace(".”", "”.")
    if "\"" in text: text = text.replace(".\"", "\".")
    if "!" in text: text = text.replace("!\"", "\"!")
    if "?" in text: text = text.replace("?\"", "\"?")
    text = text.replace(".", ".<stop>")
    text = text.replace("?", "?<stop>")
    text = text.replace("!", "!<stop>")
    text = text.replace("<prd>", ".")
    text = text.split("<stop>")
    result = text[:-1]
    return [s.strip() for s in result]


def nltk_splitter(filepath):
    result = nltk.tokenize.sent_tokenize(file_reading(filepath), "french")
    return result


def spacy_splitter(filepath):
    pipeline = spacy.load('fr_dep_news_trf')
    result = pipeline(file_reading(filepath))
    return list(result.sents)


def koehn_splitter(filepath):
    splitter = SentenceSplitter(language='fr')
    result = splitter.split(text=file_reading(filepath))
    return result


def stanford_splitter(filepath):
    pipeline = stanza.Pipeline(lang='fr', processors='tokenize')  # lang='wo' also available for wolof
    result = pipeline(file_reading(filepath))
    return [sentence.text for sentence in result.sentences]


def trankit_splitter(filepath):
    pipeline = Pipeline('french', cache_dir='../venv/lib/python3.8/site-packages/trankit/cache')
    result = pipeline.ssplit(file_reading(filepath))
    return [sentence['text'] for sentence in result['sentences']]


if __name__ == "__main__":
    file = "../text_scrapped/coran/fr/echantillon_fr.txt"
    sentences = koehn_splitter(file)
    print(len(sentences))
    print(sentences)
