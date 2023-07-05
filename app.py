from flask_restful import Api, Resource, reqparse
from flask import Flask, jsonify
import psycopg2
import time
import functions as f

# Ожидаем полное поднятие БД в докере
time.sleep(5)

# Подключение к базе данных
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="mypassword",
    host="app_db",
    port="5432"
)

count_id = 1
app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_request():
    global count_id
    parser = reqparse.RequestParser()
    parser.add_argument("kad_number")
    parser.add_argument("latitude")
    parser.add_argument("longitude")
    params = parser.parse_args()

    # Проверяем, все ли нужные поля заполнены
    if f.is_none(params):
        return jsonify({"message": "Bad request"})

    # Проверяем формат введеных координат
    if f.check_coordinates(params):
        return jsonify({"message": "Bad coordinates"})

    # Проверяем формат кадастрового номера
    if f.check_kad_num(params):
        return jsonify({"message": "Bad kad_num"})

    cur = conn.cursor()
    cur.execute("INSERT INTO requests (id, kad_number, latitude, longitude, calculate) "
                "VALUES (%s, %s, %s, %s, 'True')", (count_id, params["kad_number"], params["latitude"], params["longitude"]))

    cur.close()
    count_id += 1
    return jsonify({"id":count_id - 1})

@app.route('/get', methods=['POST'])
def get_request():
    parser = reqparse.RequestParser()
    parser.add_argument("id")
    params = parser.parse_args()

    # Проверяем, передается ли поле id
    if f.is_none_id(params):
        return jsonify({"message": "Bad request"})

    cur = conn.cursor()
    cur.execute("SELECT kad_number, latitude, longitude, calculate FROM requests "
                         "WHERE id = %s", params["id"])
    row = cur.fetchone()
    cur.close()

    if row:
        result = {
            "kad_number": row[0],
            "latitude": row[1],
            "longitude": row[2],
            "calculate": row[3]
        }
        return jsonify(result)
    else:
        return jsonify({"message": "Request not found"})

if __name__ == '__main__':
    app.run(host='0.0.0.0')