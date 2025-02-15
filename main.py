from flask import Flask
import os
import psycopg2


app = Flask(__name__)

@app.route('/')
def index():
    db_host = os.getenv('DB_HOST','127,')
    db_port = int(os.getenv('DB_PORT','5432'))
    db_name = os.getenv('DB_NAME','postgres')
    db_user = os.getenv('DB_USER','postgres')
    db_password = os.getenv('DB_PASSWORD','postgres')
    connection = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )
    cursor = connection.cursor()
    cursor.execute('SELECT id, message FROM messages')

    messages = ''
    for row in cursor.fetchall():
        messages += f'id: {row[0]}, message: {row[1]}<br>'
    connection.close()

    return messages