import glob
import chardet


def get_encoding(directory):
    for filename in glob.glob(directory + "/*.txt"):
        with open(filename, 'rb') as rawdata:
            result = chardet.detect(rawdata.read())
        print(filename.ljust(45), result['encoding'])


def merge_txt(directory, file_name):
    for file_path in glob.glob(directory + '/*.txt'):
        with open(file_path, 'r', encoding='utf-8-sig') as input_file:
            with open("C:/Users/ee591997/Desktop/Wolof_Corpus/text_scrapped" + file_name, 'a', encoding='utf-8-sig') as output_file:
                for line in input_file:
                    output_file.write(line)


# get_encoding("text_scrapped/bible/frasbl_readaloud")
# get_encoding("text_scrapped/bible/wolKYG_readaloud")
merge_txt("C:/Users/ee591997/Desktop/Wolof_Corpus/text_scrapped/bible/frasbl_readaloud", "/bible_fr.txt")
merge_txt("C:/Users/ee591997/Desktop/Wolof_Corpus/text_scrapped/bible/wolKYG_readaloud", "/bible_wol.txt")
