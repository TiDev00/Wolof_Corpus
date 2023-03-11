import subprocess


def aligner(source_lang, target_lang, target_filepath):
    hunalign_path = '../../hunalign_1.2/src/hunalign/hunalign'
    dictionary_path = '../../hunalign_1.2/data/null.dic'

    subprocess.call([hunalign_path, dictionary_path, source_lang, target_lang,
                    '-text', '>', target_filepath], shell=True)

    # subprocess.call([hunalign_path, dictionary_path, source_lang, target_lang,
    #                  '-text', '-bisent', '>', target_filepath], shell=True)


if __name__ == "__main__":
    aligner('../text_scrapped/religious/coran/fr/processed_fr_cor.txt',
            '../text_scrapped/religious/coran/wol/processed_wol_cor.txt',
            '../text_scrapped/religious/coran/cor_sentence_alignment.txt')

    aligner('../text_scrapped/religious/bible/fr/processed_fr_bib.txt',
            '../text_scrapped/religious/bible/wol/processed_wol_bib.txt',
            '../text_scrapped/religious/bible/bib_sentence_alignment.txt')

    # aligner('../text_scrapped/religious/coran/fr/processed_fr_cor.txt',
    #         '../text_scrapped/religious/coran/wol/processed_wol_cor.txt',
    #         '../text_scrapped/religious/coran/cor_1sentence_alignment.txt')
    #
    # aligner('../text_scrapped/religious/bible/fr/processed_fr_bib.txt',
    #         '../text_scrapped/religious/bible/wol/processed_wol_bib.txt',
    #         '../text_scrapped/religious/bible/bib_1sentence_alignment.txt')
