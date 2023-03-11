from csv_processings import output_generation


def score_suppression(filepath):
    data = open(filepath).readlines()
    fr_sentences = []
    wol_sentences = []
    for line in data:
        fr_sentences.append(line.split('\t')[0])
        wol_sentences.append(line.split('\t')[1])
    return fr_sentences, wol_sentences


if __name__ == '__main__':
    cor_file = score_suppression('../text_scrapped/religious/coran/cor_1sentence_alignment.txt')
    bib_file = score_suppression('../text_scrapped/religious/bible/bib_1sentence_alignment.txt')

    output_generation(cor_file[0], '../text_scrapped/religious/coran/aligned_fr_cor.txt')
    output_generation(cor_file[1], '../text_scrapped/religious/coran/aligned_wol_cor.txt')
    output_generation(bib_file[0], '../text_scrapped/religious/bible/aligned_fr_bib.txt')
    output_generation(bib_file[1], '../text_scrapped/religious/bible/aligned_wol_bib.txt')
