# # Select all rows in bible_fr table
# SELECT * FROM fr_bib;
#
# # Select all rows in bible_wol table
# SELECT * FROM wol_bib;
#
# # Select all verses containig other verses in bible_wol table
# SELECT * FROM wol_bib WHERE wol_bib.startVerse != wol_bib.endVerse;
#
# # Select all verses containig other verses in bible_fr table
# SELECT * FROM fr_bib WHERE fr_bib.startVerse != fr_bib.endVerse;
#
# # Select verses in bible_wol table and not in bible_fr table
# SELECT * FROM wol_bib WHERE wol_bib.canon_order NOT IN (SELECT fr_bib.canon_order FROM fr_bib);

# # Select verses in bible_fr table and not in bible_wol table
# SELECT * FROM fr_bib WHERE fr_bib.canon_order NOT IN (SELECT wol_bib.canon_order FROM wol_bib);

# # delete verse in bible_fr table and not bible_wol table
# DELETE FROM fr_bib WHERE fr_bib.canon_order NOT IN (SELECT wol_bib.canon_order FROM wol_bib);

# # Select and order by canon_order, chapter and startverse
# SELECT * FROM fr_bib ORDER BY canon_order, chapter, startVerse

# delete underscore contained in canon_order column in bible_fr table
# UPDATE bible.fr_bib SET canon_order = REPLACE(canon_order,'_','');

# # delete underscore contained in canon_order column in bible_wol table
# UPDATE bible.wol_bib SET canon_order = REPLACE(canon_order,'_','');
#
# # Modify canon_order column datatype in bible_fr table
# ALTER TABLE bible.fr_bib MODIFY COLUMN canon_order INT(12);
#
# # Modify canon_order column datatype in bible_wol table
# ALTER TABLE bible.wol_bib MODIFY COLUMN canon_order INT(12);

