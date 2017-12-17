import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style

style.use('ggplot')


conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def data_entry():
     c.execute("INSERT INTO stuffToPlot VALUES(145342352, '2016-01-02', 'Python', 56)")
     conn.commit()
     c.close()
     conn.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,100)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)", (unix, date, keyword, 56))
    conn.commit()

def read_from_db():
    c.execute("SELECT keyword, value, unix FROM stuffToPlot WHERE value < 50 AND keyword = 'Python'")
    # data = c.fetchall()
    # print(data)
    for row in c.fetchall():
        print(row)


def graph_data():
    c.execute("SELECT unix, value FROM stuffToPlot")
    dates = []
    values = []
    for row in c.fetchall():
        # print(row[0])
        # print(datetime.datetime.fromtimestamp(row[0]))
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])

    plt.plot_date(dates, values, '-')
    plt.show()


def del_and_update():
    c.execute("SELECT * FROM stuffToPlot")
    [print(row) for row in c.fetchall()]

    #UPDATE
    # c.execute('UPDATE stuffToPlot SET value = 99 WHERE value=34')
    # conn.commit()
    # print("")
    # c.execute("SELECT * FROM stuffToPlot")
    # [print(row) for row in c.fetchall()]

    #DELETE
    # c.execute("DELETE FROM stuffToPlot WHERE value = 99")
    # conn.commit()
    print("")
    c.execute("SELECT * FROM stuffToPlot WHERE value = 56")
    [print(row) for row in c.fetchall()]

    c.execute("SELECT * FROM stuffToPlot WHERE value = 56")
    print(len(c.fetchall()))


# read_from_db()
# create_table()
# data_entry()

# for i in range(10):
#     dynamic_data_entry()
#     time.sleep(1)

#graph_data()

del_and_update()

c.close()
conn.close()





