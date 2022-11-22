# -*- coding: utf-8 -*-

import time
import nltk
import re
import spacy
import stanza
from trankit import Pipeline
from sentence_splitter import SentenceSplitter
from mosestokenizer import MosesPunctuationNormalizer


def file_reading(filepath):
    normalized_data = []
    with open(filepath, encoding='utf-8') as f:
        raw_data = f.readlines()
    with MosesPunctuationNormalizer('fr') as normalize:
        for line in raw_data:
            normalized_data.append(normalize(line).strip())
    return ' '.join(normalized_data)


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
    return [token.strip() for token in result]


def nltk_splitter(filepath):
    result = nltk.tokenize.sent_tokenize(file_reading(filepath), "french")
    return result


def spacy_splitter(filepath):
    nlp = spacy.load('fr_dep_news_trf')
    result = nlp(file_reading(filepath))
    return [r.text for r in result.sents]


def koehn_splitter(filepath):
    splitter = SentenceSplitter(language='fr')
    result = splitter.split(text=file_reading(filepath))
    return result


def stanford_splitter(filepath):
    pipeline = stanza.Pipeline(lang='wo', processors='tokenize')  # lang='wo' also available for wolof
    result = pipeline(file_reading(filepath))
    return [token.text for token in result.sentences]


def trankit_splitter(filepath):
    pipeline = Pipeline(lang='french', embedding='xlm-roberta-large',
                        cache_dir='../venv/lib/python3.8/site-packages/trankit/cache')
    result = pipeline.ssplit(file_reading(filepath))
    return [token['text'] for token in result['sentences']]


if __name__ == "__main__":
    file = "../text_scrapped/bible/input.txt"
    # start_time = time.time()
    sentences = nltk_splitter(file)
    # end_time = time.time()
    with open('../text_scrapped/bible/output_nltk_wo.txt', 'w', encoding='utf-8') as f:
        for sentence in sentences:
            f.write(sentence + '\n')
    # print(end_time - start_time)
    print(len(sentences))
