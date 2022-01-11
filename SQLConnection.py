import pandas as pd
import sqlite3
import datetime as dt

conn = sqlite3.connect('TicTacToeRecords.db')

cur = conn.cursor()

# cur.execute('''
# Create table games (gametimestamp text, player1 text, player2 text, p1win int, p2win int, draw int)
# '''
# )

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

# update_games_log('Ben', 'Nick', 'Ben')
# update_games_log('Ben', 'Nick', 'Nick')
# update_games_log('Ben', 'Nick', 'Ben')

# update_games_log('Ben', 'Nick', 'Ben')
# update_games_log('Ben', 'Nick', 'Nick')


def Top10Wins(conn):  
    cur = conn.cursor() 

    cur.execute('''
        create table Player1Wins as select distinct
            player1 as player, 
            sum(p1win) as winner
        from
            games 
        where 
            p1win = 1
        group by
            player1
    ''')

    cur.execute('''
        create table Player2Wins as select distinct
            player2 as player, 
            sum(p2win) as winner
        from
            games 
        where
            p2win = 1
        group by
            player2
    ''')

    cur.execute('''
        create table PlayerWins as 
            select * from Player1Wins
        union select * from Player2Wins
    ''')

    cur.execute('''
        create table Top10Wins as select distinct
            player, 
            sum(winner) as GamesWon
        from
            PlayerWins
        group by
            player
        order by
            GamesWon Desc
        Limit 10
    ''')


    df = pd.read_sql_query('''select * from Top10Wins''', con = conn)

    cur.execute('''drop table Player1Wins''')
    cur.execute('''drop table Player2Wins''')
    cur.execute('''drop table PlayerWins''')
    cur.execute('''drop table Top10Wins''')

    return df