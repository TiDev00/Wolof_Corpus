import os
import glob


def all_text_in_one(directory):
    list_of_files = sorted(filter(os.path.isfile, glob.glob(directory + '/*')))
    for file_path in list_of_files:
        with open(file_path, 'r', encoding='utf-8') as input_file:
            with open('bible_fr.txt', 'a') as output_file:
                output_file.seek(0)
                for line in input_file:
                    output_file.write(line)


all_text_in_one('src_lang/frasbl_readaloud')


all_text_in_one('src_lang/wolKYG_readaloud')
