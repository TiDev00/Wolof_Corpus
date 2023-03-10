import subprocess


def aligner(source_lang, target_lang, target_filepath):
    hunalign_path = '../../hunalign_1.2/src/hunalign/hunalign'
    dictionary_path = '../../hunalign_1.2/data/null.dic'

    subprocess.call([hunalign_path, dictionary_path, source_lang, target_lang,
                    '-text', '>', target_filepath], shell=True)

    # subprocess.call([hunalign_path, dictionary_path, source_lang, target_lang,
    #                  '-text', '-bisent', '>', target_filepath], shell=True)


if __name__ == "__main__":
    aligner('../text_scrapped/religious/coran/fr_cor.txt',
            '../text_scrapped/religious/coran/wol_cor.txt',
            '../text_scrapped/religious/coran/aligned_cor.txt')

    aligner('../text_scrapped/religious/bible/fr_bib.txt',
            '../text_scrapped/religious/bible/wol_bib.txt',
            '../text_scrapped/religious/bible/aligned_bib.txt')
