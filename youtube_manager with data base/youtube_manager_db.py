import sqlite3

connection = sqlite3.connect('youtube_videos.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS youtube_videos
                  (id INTEGER PRIMARY KEY, title TEXT NOT NULL, views INTEGER, likes INTEGER)''')