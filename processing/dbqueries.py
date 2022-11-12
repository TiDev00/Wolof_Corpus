import mysql.connector

configs = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
    'database': 'bible',
    'raise_on_warnings': True
}

fr_select = "SELECT * FROM fr_bib"
wol_select = "SELECT * FROM wol_bib"
wol_mult_verse = "SELECT * FROM wol_bib WHERE wol_bib.startVerse != wol_bib.endVerse"
fr_mult_verse = "SELECT * FROM fr_bib WHERE fr_bib.startVerse != fr_bib.endVerse"
wol_verse_not_in_fr_bib = "SELECT * FROM wol_bib WHERE wol_bib.verseID NOT IN (SELECT fr_bib.verseID FROM fr_bib)"
fr_verse_not_in_wol_bib = "SELECT * FROM fr_bib WHERE fr_bib.verseID NOT IN (SELECT wol_bib.verseID FROM wol_bib)"
delete_fr_verse_not_in_wol_bib = "DELETE FROM fr_bib WHERE fr_bib.verseID NOT IN (SELECT wol_bib.verseID FROM wol_bib)"


conn = mysql.connector.connect(**configs)

cursor = conn.cursor(dictionary=True)
cursor.execute(fr_select)

results = cursor.fetchall()

for item in results:
    print(item)

conn.close()
