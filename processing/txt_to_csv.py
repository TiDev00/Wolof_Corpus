def convertor(filepath, output_filepath):
    data = open(filepath).readlines()

    sourates_list = []

    for verses in data:
        sourates_list.append((verses.rstrip().split('|')[0], verses.rstrip().split('|')[1]))

    sourates_dict = {}
    for key, values in sourates_list:
        sourates_dict.setdefault(key, []).append(values)

    with open(output_filepath, 'w') as f:
        f.write("{},{},{},{}\n".format('SourateID', 'Sourate', 'VerseID', 'Verse'))
        for sourate, verses in sourates_dict.items():
            for verse in verses:
                f.write("{},{},{},\"{}\"\n".format(list(sourates_dict).index(sourate) + 1, sourate,
                                                   verses.index(verse) + 1, verse))


convertor('../text_scrapped/religious/coran/fr/coran_fr.txt', '../text_scrapped/religious/coran/fr/coran_fr.csv')
convertor('../text_scrapped/religious/coran/wol/coran_wol.txt', '../text_scrapped/religious/coran/wol/coran_wol.csv')
