import os
import glob


def all_text_in_one(directory):
    list_of_files = sorted(filter(os.path.isfile, glob.glob(directory + '/*')))
    for file_path in list_of_files:
        with open(file_path, 'r', encoding='utf-8') as input_file:
            with open('bible_wol.txt', 'a') as output_file:
                output_file.seek(0)
                for line in input_file:
                    output_file.write(line)


def number_of_line(directory):
    list_of_files = sorted(filter(os.path.isfile, glob.glob(directory + '/*')))
    for file_path in list_of_files:
        count_line = 0
        for line in file_path:
            count_line += 1
        print("{0} = {1}".format(file_path, count_line))
