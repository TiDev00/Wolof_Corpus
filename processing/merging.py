import glob
import chardet
import xml.etree.ElementTree as ET


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
                    output_file.write(line)


def xml_processing(directory1):
    file1 = ET.parse(directory1)
    root1 = file1.getroot()
    for child1 in root1:
        print(child1.attrib)

# num_line("C:/Users/mkdiallo/Desktop/Wolof_Corpus/text_scrapped/bible/frasbl_readaloud")
# num_line("C:/Users/mkdiallo/Desktop/Wolof_Corpus/text_scrapped/bible/wolKYG_readaloud")
# # get_encoding("text_scrapped/bible/vpl/frasbl_vpl")
# get_encoding("text_scrapped/bible/vpl/wolKYG_vpl")
# get_encoding("text_scrapped/bible/txt/frasbl_readaloud")
# get_encoding("text_scrapped/bible/txt/wolKYG_readaloud")
# merge_txt("text_scrapped/bible/frasbl_readaloud", "/bible_fr.txt")
# merge_txt("text_scrapped/bible/wolKYG_readaloud", "/bible_wol.txt")
# xml_processing("text_scrapped/bible/vpl/frasbl_vpl/frasbl_vpl.xml")
