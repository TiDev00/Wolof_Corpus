# Select all rows in bible_fr table
SELECT * FROM fr_bib;

# Select all rows in bible_wol table
SELECT * FROM wol_bib;

# Select all verses containing other verses in bible_wol table
SELECT * FROM wol_bib WHERE wol_bib.startVerse != wol_bib.endVerse;

# Select all verses containing other verses in bible_fr table
SELECT * FROM fr_bib WHERE fr_bib.startVerse != fr_bib.endVerse;

# Select verses in bible_wol table and not in bible_fr table
SELECT * FROM wol_bib WHERE wol_bib.canon_order NOT IN (SELECT fr_bib.canon_order FROM fr_bib);

# Select verses in bible_fr table and not in bible_wol table
SELECT * FROM fr_bib WHERE fr_bib.canon_order NOT IN (SELECT wol_bib.canon_order FROM wol_bib);

# delete verse in bible_fr table and not in bible_wol table
DELETE FROM fr_bib WHERE fr_bib.canon_order NOT IN (SELECT wol_bib.canon_order FROM wol_bib);

# delete leading and trailing \n in verseText fr_bib.verseText column
UPDATE bible.fr_bib SET verseText = TRIM('\n' FROM verseText);

# delete leading and trailing \n in verseText wol_bib.verseText column
UPDATE bible.fr_bib SET verseText = TRIM('\n' FROM verseText);
