import random


def output_generation(content, outfile_wo, outfile_fr):
    with open(outfile_wo, 'w') as f_wo, open(outfile_fr, 'w') as f_fr:
        for sentence_wo, sentence_fr in content:
            f_wo.write(sentence_wo + '\n')
            f_fr.write(sentence_fr + '\n')


def splitter(source, target):
    combined_data = []
    with open(source, 'r') as f_wo, open(target, 'r') as f_fr:
        for line_wo, line_fr in zip(f_wo, f_fr):
            combined_data.append((line_wo.strip(), line_fr.strip()))

    random.shuffle(combined_data)

    test_size = 4050

    return combined_data[test_size:], \
           combined_data[:test_size]


if __name__ == '__main__':
    train_data, test_data = splitter('../text_scrapped/merged_corpus.wo', '../text_scrapped/merged_corpus.fr')
    output_generation(train_data, '../train.wo', '../train.fr')
    output_generation(test_data, '../test.wo', '../test.fr')
