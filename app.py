from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_consultas"
)
cursor = db.cursor()


@app.route('/data', methods=['GET'])
def get_data():
    cursor.execute("SELECT * FROM asistencia")
    data = cursor.fetchall()
    return jsonify({'data': data})


if __name__ == '__main__':
    app.run(debug=True)
