import sqlite3

db = sqlite3.connect('animetitans.db')
cr = db.cursor()


# animes
cr.execute('SELECT * FROM Animes')
animes = cr.fetchall()


def Animes():
    return animes


# episodes
cr.execute('SELECT * FROM Episodes')
episodes = cr.fetchall()


def Episodes():
    return episodes


# categorie
cr.execute('SELECT * FROM Categories')
categories = cr.fetchall()


def Categories():
    return categories



db.close()
