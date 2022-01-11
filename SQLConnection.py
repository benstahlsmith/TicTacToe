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


def update_games_log(p1, p2, winner):
    time = str(dt.datetime.now())
    if p1 == winner:
        cur.execute(f'''
        insert into games values ('{time}', '{p1}', '{p2}', 1,0,0)
        ''')
    if p2 == winner:
        cur.execute(f'''
        insert into games values ('{time}', '{p1}', '{p2}', 0,1,0)
        ''')
    else:
        cur.execute(f'''
        insert into games values ('{time}', '{p1}', '{p2}', 0,0,1)
        ''')

    conn.commit()

update_games_log('Ben', 'Nick', 'Ben')
update_games_log('Ben', 'Nick', 'Nick')
update_games_log('Ben', 'Nick', 'Ben')


cur.execute('''
    create table Player1Wins as select 
        player1, 
        p1win
    from
        games 
''')

cur.execute('''
    create table Player2Wins as select 
        player2, 
        p2win
    from
        games 
''')



print(pd.read_sql_query('''select * from Player2Wins''', con = conn))

cur.execute('''drop table Player1Wins''')
cur.execute('''drop table Player2Wins''')