# import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="swiperz_db",
        user='swiperz',
        password='swiperz')

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS games;')
cur.execute('CREATE TABLE games (id serial PRIMARY KEY,'
                                 'player1 varchar (150) NOT NULL,'
                                 'player2 varchar (150) NOT NULL,'
                                 'game_over varchar (150) NOT NULL DEFAULT FALSE,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

# Insert data into the table

cur.execute('INSERT INTO games (player1, player2, game_over)'
            'VALUES (%s, %s, %s)',
            ('marc',
             'wenyan',
             'true')
            )

cur.execute('INSERT INTO games (player1, player2, game_over)'
            'VALUES (%s, %s, %s)',
            ('bob',
             'bill',
             'false')
            )

conn.commit()

cur.close()
conn.close()