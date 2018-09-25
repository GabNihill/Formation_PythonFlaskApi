import sqlite3
from sqlite3 import Error
import datetime


def get_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_connection(db_file):
    """create a database connection to a SQlite database"""
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
    return None


def create_table(conn, create_table_sql):
    """create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:"""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_people(conn, people):
    """
    Create a new people into the peoples table
    :param conn: the connection object
    :param people: people object
    :return: people ID
    """

    lastname = people[0]
    firstname = people[1]
    list = [lastname, firstname]

    sql = '''INSERT OR IGNORE INTO peoples(lname, fname, timestamp)
                VALUES(?, ? , ?)'''
    cur = conn.cursor()
    cur.execute(sql, people)
    return cur.lastrowid


def update_people(conn, people):
    """
    Update fname, lname and timestamp of a people
    :param conn: the connection object
    :param people: people object
    :return:
    """
    sql = ''' UPDATE peoples
                SET lname = ?,
                    fname = ?,
                    timestamp = ?
                WHERE rowid = ?'''
    cur = conn.cursor()
    cur.execute(sql, people)

def delete_people(conn, rowid):
    """
    Delete a people by his rowid
    :param conn: the connection object
    :param rowid: table row id
    :return:
    """
    sql = 'DELETE FROM peoples WHERE rowid = ?'
    cur = conn.cursor()
    cur.execute(sql, (rowid,))

def delete_all_people(conn):
    """
    Delete all rows in peoples table
    :param conn: the connection object
    :return:
    """
    sql = "DELETE FROM peoples"
    cur = conn.cursor()
    cur.execute(sql)

def select_all_peoples(conn):
    """
    Query all rows in the peoples table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM peoples")
    rows = cur.fetchall()

    for row in rows:
        print(row)
    return rows


def select_people_by_lname(conn, lname):
    """
    Query people by last name
    :param conn: connection object
    :param lname: last name
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM peoples WHERE lname=?", (lname,))

    rows = cur.fetchall()
    for row in rows:
        print(row)
    return rows

def main():
    database = "peoples_db.db"

    sql_create_peoples_table = """CREATE TABLE IF NOT EXISTS peoples (
                                        fname TEXT, 
                                        lname TEXT,
                                        timestamp TEXT,
                                        UNIQUE(fname, lname));"""

    conn = create_connection(database)
    # with conn:
    # create_table(conn, sql_create_peoples_table)
    # people1 = ['Marino', 'Gabriel', get_timestamp()]
    # people2 = ['Di-Mambro', 'Alexandre', get_timestamp()]
    # people3 = ['Normand', 'Etienne', get_timestamp()]
    # people4 = ['Marino', 'Gabriel', get_timestamp()]
    # people5 = ['Marino', 'Meghan', get_timestamp()]
    # peoples = [people1, people2, people3, people4, people5]

if __name__ == '__main__':
    main()