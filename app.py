from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    conn = psycopg2.connect(
        dbname='ifood',
        user='ifooduser',
        password='ifoodpassword',
        host='db'
    )
    cursor = conn.cursor()
    cursor.execute('SELECT version()')
    db_version = cursor.fetchone()
    cursor.close()
    conn.close()
    return f'Conexão com PostgreSQL estabelecida. Versão do banco de dados: {db_version}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
