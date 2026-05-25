from flask import Flask, jsonify, request
import time
import random

app = Flask(__name__)
# Имитация базы данных
posts = [ 
    {"id": 1, "title": "Первый пост", "content": "Привет, мир!"}
]

@app.route('/posts', methods=['GET'])
def get_posts():
    # Имитируем небольшую задержку сервера (0.1 - 0.3 сек)
    time.sleep(random.uniform(0.1, 0.3))
    return jsonify(posts)

@app.route('/posts', methods=['POST'])
def create_post():
    # Имитируем более долгую обработку при записи
    time.sleep(random.uniform(0.2, 0.5))
    data = request.json
    posts.append(data)
    return jsonify({"status": "created"}), 201

if __name__ == '__main__':
    app.run(port=5000)