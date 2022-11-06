from pathlib import Path
import re
from sentence_splitter import SentenceSplitter


def read_file(directory):
    text = " "
    with open(directory, 'r', encoding='utf-8-sig') as input_file:
        for line in input_file:
            re.sub('\n', ' ', line)
            re.sub(' ', ' ', line)
            text = text + ' ' + line
        print(text)


read_file("C:/Users/mkdiallo/Desktop/004_LEV_14_read.txt")
# Object interface
splitter = SentenceSplitter(language='fr')
# print(splitter.split(text=read_file("C:/Users/mkdiallo/Desktop/004_LEV_14_read.txt")))


# Functional interface
# print(split_text_into_sentences(
#     text='This is a paragraph. It contains several sentences. "But why," you ask?',
#     language='en'
# ))
