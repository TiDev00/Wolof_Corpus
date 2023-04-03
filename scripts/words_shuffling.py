import random


def shuffle_sentences(input_file_path, output_file_path, num_lines):
    # Open the input file and create an output file
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        # Process the first 10,000 lines
        for i in range(num_lines):
            # Read a line from the input file
            line = input_file.readline().strip()

            # Split the line into a list of words
            words = line.split()

            # Shuffle the list of words
            random.shuffle(words)

            # Join the shuffled words back into a sentence and write it to the output file
            shuffled_line = ' '.join(words) + '\n'
            output_file.write(shuffled_line)


shuffle_sentences('../final_corpora/correction_task/corpus.err', '../final_corpora/correction_task/inv.txt', 10000)
