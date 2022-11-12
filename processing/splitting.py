from pathlib import Path
import re
from sentence_splitter import SentenceSplitter

# read_file("C:/Users/mkdiallo/Desktop/004_LEV_14_read.txt")
# Object interface
splitter = SentenceSplitter(language='fr')
print(splitter.split(text=""""""))


# Functional interface
# print(split_text_into_sentences(
#     text='This is a paragraph. It contains several sentences. "But why," you ask?',
#     language='en'
# ))

