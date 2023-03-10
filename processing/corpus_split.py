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

    # random.shuffle(combined_data)

    num_sentences = len(combined_data)
    train_size = int(num_sentences * train_ratio)
    dev_size = int(num_sentences * dev_ratio) + 1

    return combined_data[:train_size], \
            combined_data[train_size:train_size + dev_size], \
            combined_data[train_size + dev_size:]


if __name__ == '__main__':
    train_data, dev_data, test_data = splitter('../text_scrapped/religious/wol_rel.txt',
                                                '../text_scrapped/religious/fr_rel.txt')
    output_generation(train_data, '../train.wo', '../train.fr')
    output_generation(dev_data, '../dev.wo', '../dev.fr')
    output_generation(test_data, '../test.wo', '../test.fr')
