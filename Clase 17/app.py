from flask import Flask, request, jsonify, Response
import redis
import uuid
import time
from prometheus_client import Counter, Histogram, generate_latest
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

r = redis.StrictRedis(host='redis', port=6379, db=0)

# reseñas totales
review_counter = Counter('reviews_total', 'Total number of reviews posted')

# juegos creados
games_created_counter = Counter('games_created_total', 'Total number of games created')

# registros de usuario (simulado)
user_registrations_counter = Counter('user_registrations_total', 'Total number of users registered')

# peticiones http por endpoint y método
api_requests_counter = Counter(
    'api_requests_total',
    'Total number of HTTP requests',
    ['endpoint', 'method']
)

# endpoint - latencia
request_duration = Histogram(
    'api_request_duration_seconds',
    'Request latency by endpoint',
    ['endpoint']
)

@app.route('/', methods=['GET'])
def test():
    api_requests_counter.labels(endpoint="/", method="GET").inc()
    return jsonify({"message": "Todo bien"}), 200

@app.route('/games', methods=['POST'])
def create_game():
    api_requests_counter.labels(endpoint="/games", method="POST").inc()
    with request_duration.labels(endpoint="/games").time():
        data = request.json
        game_id = str(uuid.uuid4())
        r.hmset(f'game:{game_id}', data)
        r.sadd('all_game_ids', game_id)
        games_created_counter.inc()
        return jsonify({"message": "Juego creado", "game_id": game_id}), 201

@app.route('/games', methods=['GET'])
def get_all_games():
    api_requests_counter.labels(endpoint="/games", method="GET").inc()
    with request_duration.labels(endpoint="/games").time():
        game_ids = r.smembers('all_game_ids')
        games = []
        for game_id_byte in game_ids:
            game_id = game_id_byte.decode()
            game_data = r.hgetall(f'game:{game_id}')
            if game_data:
                game_info = {k.decode(): v.decode() for k, v in game_data.items()}
                game_info['id'] = game_id
                games.append(game_info)
        return jsonify(games)

@app.route('/games/<game_id>', methods=['GET'])
def get_game(game_id):
    api_requests_counter.labels(endpoint="/games/<game_id>", method="GET").inc()
    with request_duration.labels(endpoint="/games/<game_id>").time():
        game = r.hgetall(f'game:{game_id}')
        if not game:
            return jsonify({"message": "Juego no encontrado"}), 404
        return jsonify({k.decode(): v.decode() for k, v in game.items()})

@app.route('/games/<game_id>/reviews', methods=['POST'])
def add_review(game_id):
    api_requests_counter.labels(endpoint="/games/<game_id>/reviews", method="POST").inc()
    with request_duration.labels(endpoint="/games/<game_id>/reviews").time():
        if not r.exists(f'game:{game_id}'):
            return jsonify({"message": "Juego no encontrado"}), 404
        data = request.json
        review_id = str(uuid.uuid4())
        timestamp = int(time.time())
        review_data = {
            "game_id": game_id,
            "user_id": data.get("user_id", "anonymous"),
            "score": data.get("score"),
            "comment": data.get("comment"),
            "timestamp": timestamp
        }
        r.hmset(f'review:{review_id}', review_data)
        r.rpush(f'game:{game_id}:reviews', review_id)
        review_counter.inc()
        return jsonify({"message": "Reseña añadida", "review_id": review_id}), 201

@app.route('/games/<game_id>/reviews', methods=['GET'])
def get_game_reviews(game_id):
    api_requests_counter.labels(endpoint="/games/<game_id>/reviews", method="GET").inc()
    with request_duration.labels(endpoint="/games/<game_id>/reviews").time():
        if not r.exists(f'game:{game_id}'):
            return jsonify({"message": "Juego no encontrado"}), 404
        review_ids = r.lrange(f'game:{game_id}:reviews', 0, -1)
        reviews = []
        for review_id in review_ids:
            review = r.hgetall(f'review:{review_id.decode()}')
            if review:
                reviews.append({k.decode(): v.decode() for k, v in review.items()})
        return jsonify(reviews)

# Simulación de registro de usuario
@app.route('/register', methods=['POST'])
def register_user():
    api_requests_counter.labels(endpoint="/register", method="POST").inc()
    with request_duration.labels(endpoint="/register").time():
        user_registrations_counter.inc()
        return jsonify({"message": "Usuario registrado"}), 201

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
