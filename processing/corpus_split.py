import random

train_ratio = 0.8
dev_ratio = 0.1


def output_generation(content, outfile_wo, outfile_fr):
    with open(outfile_wo, 'w', encoding='utf-8') as f_wo, open(outfile_fr, 'w', encoding='utf-8') as f_fr:
        for sentence_wo, sentence_fr in content:
            f_wo.write(sentence_wo + '\n')
            f_fr.write(sentence_fr + '\n')


def splitter(source, target):
    combined_data = []
    with open(source, 'r', encoding='utf-8') as f_wo, open(target, 'r', encoding='utf-8') as f_fr:
        for line_wo, line_fr in zip(f_wo, f_fr):
            combined_data.append((line_wo.strip(), line_fr.strip()))

    random.shuffle(combined_data)

    num_sentences = len(combined_data)
    train_size = int(num_sentences * train_ratio) + 1

    return combined_data[:train_size], combined_data[train_size:]


if __name__ == '__main__':
    train_data, test_data = splitter('../text_scrapped/wol_corpus.txt',
                                                '../text_scrapped/fr_corpus.txt')
    output_generation(train_data, '../train.wo', '../train.fr')
    output_generation(test_data, '../test.wo', '../test.fr')
