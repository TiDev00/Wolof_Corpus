import glob
import chardet


def num_line(directory):
    for file_path in sorted(glob.glob(directory + '/*')):
        with open(file_path, 'r', encoding='utf-8-sig') as filename:
            print("{0} = {1}".format(file_path, len(filename.readlines())))


def get_encoding(directory):
    for filename in sorted(glob.glob(directory + "/*.txt")):
        with open(filename, 'rb') as rawdata:
            result = chardet.detect(rawdata.read())
        print(filename.ljust(45), result['encoding'])


def merge_txt(directory, file_name):
    for file_path in sorted(glob.glob(directory + '/*.txt')):
        with open(file_path, 'r', encoding='utf-8-sig') as input_file:
            with open("text_scrapped" + file_name, 'a',
                      encoding='utf-8-sig') as output_file:
                for line in input_file:
                    line.replace('NBSP')
                    output_file.write(line)


# num_line("C:/Users/mkdiallo/Desktop/Wolof_Corpus/text_scrapped/bible/frasbl_readaloud")
# num_line("C:/Users/mkdiallo/Desktop/Wolof_Corpus/text_scrapped/bible/wolKYG_readaloud")
# get_encoding("text_scrapped/bible/frasbl_readaloud")
# get_encoding("text_scrapped/bible/wolKYG_readaloud")
# merge_txt("text_scrapped/bible/frasbl_readaloud", "/bible_fr.txt")
# merge_txt("text_scrapped/bible/wolKYG_readaloud", "/bible_wol.txt")
