import datetime

import mysql.connector

host = "213.165.95.21"
user = "root"
pwd = "password"
database = "economy"


def create_user(id):
    conn = mysql.connector.connect(
        host='213.165.95.218',
        user='root',
        password='password',
        database='economy'
    )
    cursor = conn.cursor()
    sql = "INSERT INTO users (id) " \
          f"VALUES (%s)"
    values = (id,)
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()


def delete_user(id):
    conn = mysql.connector.connect(
        host='213.165.95.218',
        user='root',
        password='password',
        database='economy'
    )
    cursor = conn.cursor()
    sql = "DELETE FROM users WHERE id=%s"
    values = (id,)
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()


def get_balance(id):
    conn = mysql.connector.connect(
        host='213.165.95.218',
        user='root',
        password='password',
        database='economy'
    )
    cursor = conn.cursor()
    sql = "select balance from users where id=%s"
    values = (id,)
    cursor.execute(sql, values)

    balance = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return balance


def set_balance(id, balance):
    conn = mysql.connector.connect(
        host='213.165.95.218',
        user='root',
        password='password',
        database='economy'
    )
    cursor = conn.cursor()
    sql = "UPDATE users SET balance=%s WHERE id=%s"
    values = (balance, id)
    cursor.execute(sql, values)

    conn.commit()
    cursor.close()
    conn.close()


def get_last_daily(id):
    conn = mysql.connector.connect(
        host='213.165.95.218',
        user='root',
        password='password',
        database='economy'
    )
    cursor = conn.cursor()
    sql = "SELECT last_daily FROM users WHERE id=%s"
    values = (id,)
    cursor.execute(sql, values)

    timestamp = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return timestamp


def set_last_daily(id):
    conn = mysql.connector.connect(
        host='213.165.95.218',
        user='root',
        password='password',
        database='economy'
    )
    cursor = conn.cursor()
    sql = "UPDATE users SET last_daily=%s WHERE id=%s"
    values = (datetime.datetime.now(), id)
    cursor.execute(sql, values)

    conn.commit()
    cursor.close()
    conn.close()


def user_exist(id):
    conn = mysql.connector.connect(
        host='213.165.95.218',
        user='root',
        password='password',
        database='economy'
    )
    cursor = conn.cursor()
    sql = "SELECT * FROM users WHERE id=%s"
    values = (id,)
    cursor.execute(sql, values)

    existing_user = cursor.fetchone()

    cursor.close()
    conn.close()

    if not existing_user:
        return False
    return True
