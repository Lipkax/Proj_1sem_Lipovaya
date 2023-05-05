import sqlite3 as sq
from zapros import *

with sq.connect('Turist.db') as con:
    cur = con.cursor()
    # cur.execute("""CREATE TABLE IF NOT EXISTS Bronirovanie(
    #  Bron_id INTEGER PRIMARY KEY AUTOINCREMENT,
    #  date_bron DATE,
    #  numb_turist INTEGER,
    #  Turists_id INTEGER,
    #  Tur_id INTEGER,
    #  FOREIGN KEY(Turists_id) REFERENCES Turists(Turists_id)
    #  FOREIGN KEY(Tur_id) REFERENCES Tur(Tur_id)
    #  )""")
    # cur.executemany("INSERT INTO Turists VALUES (?, ?, ?, ?, ?, ?, ?)", info_turists)
    # cur.executemany("INSERT INTO Tur VALUES (?, ?, ?, ?, ?, ?, ?)", info_tur)
    # cur.executemany("INSERT INTO Bronirovanie VALUES (?, ?, ?, ?, ?)", info_bron)

    # print(cur.execute("SELECT name, surname score FROM Turists").fetchall())
    # print(cur.execute("SELECT name, country, city FROM Tur ORDER BY price DESC").fetchall())
    # print(cur.execute("SELECT numb_turist FROM Bronirovanie WHERE Bron_id=4").fetchall())
    # print(cur.execute
    #       ("SELECT Turists.name, Turists.surname, Bronirovanie.date_bron FROM Turists INNER JOIN Bronirovanie ON "
    #        "Turists.Turists_id = Bronirovanie.Bron_id WHERE date_bron='2023-02-01'").fetchall())
    # print(cur.execute("SELECT name, country, city score FROM Tur ").fetchall())
    # print(cur.execute("SELECT name, surname FROM Turists WHERE sex ='ж' AND old > '1990-01-01' ").fetchall())
    # print(cur.execute("SELECT name, country, city score FROM Tur WHERE price > 5000 ").fetchall())
    # print(cur.execute("SELECT Turists.name, Turists.surname FROM Turists INNER JOIN Bronirovanie ON "
    #                   "Turists.Turists_id = Bronirovanie.Bron_id WHERE Bronirovanie.Bron_id = 3").fetchall())
    # print(cur.execute("SELECT Turists.name, Turists.surname FROM Turists INNER JOIN Bronirovanie ON "
    #                   "Turists.Turists_id = Bronirovanie.Bron_id WHERE Bronirovanie.Bron_id = 4 AND "
    #                   "Bronirovanie.date_bron = '2023-05-01' ").fetchall())
    # print(cur.execute("SELECT name, surname score FROM Turists WHERE number_phone LIKE '+7%'").fetchall())

    # cur.execute('UPDATE Tur SET start = "2023-05-01" WHERE Tur_id = 1')
    # cur.execute('UPDATE Tur SET price = 1500 WHERE Tur_id = 7')
    # cur.execute('UPDATE Turists SET number_phone = "+1 (555) 123-4567" WHERE Turists_id = 5')
    # cur.execute('UPDATE Bronirovanie SET date_bron = "2023-04-05" WHERE Tur_id = 3')
    # cur.execute('UPDATE Bronirovanie SET numb_turist = 3 WHERE Bron_id = 8')
    # cur.execute('UPDATE Tur SET expiration = "2023-08-31" WHERE Tur_id = 2')
    # cur.execute('UPDATE Turists SET email = "new_email@example.com" WHERE Turists_id = 1')
    # cur.execute('UPDATE Tur SET start = "2023-06-15" WHERE Tur_id = 4')
    # cur.execute('UPDATE Tur SET start = "2023-05-01" WHERE country = "Испания"')
    # cur.execute('UPDATE Tur SET price = 1500 WHERE name = "Греция-отдых на море" ')
    # # cur.execute('UPDATE Tur SET name="Испания - путешствие по городам" WHERE Tur_id = 9')
    # cur.execute('UPDATE Tur SET start = "2023-06-01" WHERE name = "Испания - путешствие по городам" ')
    # # cur.execute('UPDATE Bronirovanie SET Bron_id = 1002 WHERE Bron_id = 10')
    # cur.execute('UPDATE Bronirovanie SET numb_turist = 3 WHERE Bron_id = 1002')
    # # cur.execute('UPDATE Turists SET Turists_id = 2001 WHERE Turists_id = 10')
    # cur.execute('UPDATE Turists SET number_phone = "+1 (123) 456-7890" WHERE Turists_id = 2001')
    # cur.execute('UPDATE Tur SET start = "2024-07-01 " WHERE price < 2000')
    # cur.execute("UPDATE Turists SET email = 'new_email@example.com.' WHERE number_phone LIKE '+7%'")

    #1 cur.execute("DELETE FROM Bronirovanie WHERE Turists_id = 1")
    #2 cur.execute("DELETE FROM Bronirovanie WHERE Tur_id = 2")
    #3 cur.execute("DELETE FROM Bronirovanie WHERE date_bron = '2023-06-02'")
    ## cur.execute('UPDATE Bronirovanie SET Tur_id = 3 WHERE Bron_id = 8')
    #4 cur.execute("DELETE FROM Turists WHERE Turists_id = (SELECT Turists_id FROM Bronirovanie WHERE Tur_id = 3)")
    #5 cur.execute("DELETE FROM Bronirovanie WHERE Turists_id = (SELECT Turists_id FROM Turists WHERE number_phone = '+79230583730')")
    ### cur.execute('UPDATE Bronirovanie SET Turists_id = 5 WHERE Bron_id = 6')
    #6 cur.execute("DELETE FROM Bronirovanie WHERE Turists_id = (SELECT Turists_id FROM Turists WHERE email = 'test5@mail.ru')")
    #7 cur.execute("DELETE FROM Bronirovanie WHERE Tur_id = (SELECT Tur_id FROM Tur WHERE start > '2024-07-01')")
    #8 cur.execute("DELETE FROM Turists WHERE Turists_id = (SELECT Tur_id FROM Bronirovanie WHERE Turists_id=(SELECT Turists_id FROM Tur WHERE country = 'Египет'))")
    #9! cur.execute("DELETE FROM Bronirovanie WHERE Tur_id = (SELECT Tur_id FROM Tur WHERE expiration < '2023-07-30')")
    


