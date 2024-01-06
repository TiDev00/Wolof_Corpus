import csv
from sentences_splitters import koehn_splitter


def csv_to_list(filepath):
    with open(filepath) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip first row
        return [row[-1] for row in reader]


def output_generation(content, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for sentence in content:
            f.write(sentence + '\n')
        f.close()


if __name__ == '__main__':
    # Extraction from csv file
    wol_cor = csv_to_list('../text_scrapped/religious/coran/wol/wol_cor.csv')
    fr_cor = csv_to_list('../text_scrapped/religious/coran/fr/fr_cor.csv')
    wol_bib = csv_to_list('../text_scrapped/religious/bible/wol/wol_bib.csv')
    fr_bib = csv_to_list('../text_scrapped/religious/bible/fr/fr_bib.csv')

    # Sentences splittings
    wol_cor_sentences = koehn_splitter(wol_cor)
    fr_cor_sentences = koehn_splitter(fr_cor)
    wol_bib_sentences = koehn_splitter(wol_bib)
    fr_bib_sentences = koehn_splitter(fr_bib)

    # corpora generation
    output_generation(wol_cor_sentences, '../text_scrapped/religious/coran/wol/processed_wol_cor.txt')
    output_generation(fr_cor_sentences, '../text_scrapped/religious/coran/fr/processed_fr_cor.txt')
    output_generation(wol_bib_sentences, '../text_scrapped/religious/bible/wol/processed_wol_bib.txt')
    output_generation(fr_bib_sentences, '../text_scrapped/religious/bible/fr/processed_fr_bib.txt')
