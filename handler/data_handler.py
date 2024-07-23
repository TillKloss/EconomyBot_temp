import mysql.connector

host = "213.165.95.21"
user = "root"
pwd = "password"
database = "economy"


def check_db():
    conn = mysql.connector.connect(
        host='213.165.95.218',
        user='root',
        password='password',
        database='economy'
    )

    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    for table in tables:
        print(table)

    cursor.close()
    conn.close()


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

    return cursor.fetchone()[0]

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
    sql_check_user = "SELECT * FROM users WHERE id=%s"
    cursor.execute(sql_check_user, (id,))
    existing_user = cursor.fetchone()
    cursor.close()
    conn.close()
    if not existing_user:
        return False
    return True
