import random

def shuffle_sentences(input_file_path, output_file_path, num_lines):
    # Open the input and output files
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        # Process the first num_lines lines
        for i in range(num_lines):
            # Read a line from the input file
            line = next(input_file).strip()

            # Split the line into a list of words
            words = line.split()

            # Shuffle the list of words
            random.shuffle(words)

            # Join the shuffled words back into a sentence and write it to the output file
            shuffled_line = ' '.join(words) + '\n'
            output_file.write(shuffled_line)

            # Yield the shuffled sentence to free up memory
            yield shuffled_line

