import pandas as pd
import sqlite3
import datetime as dt

conn = sqlite3.connect('TicTacToeRecords.db')

cur = conn.cursor()

# cur.execute('''
# Create table games (gametimestamp text, player1 text, player2 text, p1win int, p2win int, draw int)
# '''
# )

time = str(dt.datetime.now())
print(time)
cur.execute(f'''
insert into games values ('{time}', 'Ben', 'Nick', 1,0,0)
''')

# # cur.execute('''
# # drop table games
# # ''')

conn.commit()

games = pd.read_sql_query('''
select * from games
''',  con = conn)

print(games)