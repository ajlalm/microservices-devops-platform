from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from flask import Flask, request, jsonify

app = Flask(__name__)

SERVICE_NAME = "auth-service"


REQUEST_COUNT = Counter(
    "auth_service_requests_total",
    "Total requests to auth-service"
)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "service": SERVICE_NAME,
        "status": "healthy"
    }), 200


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body must be JSON"
        }), 400

    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "admin123":
        return jsonify({
            "message": "Login successful",
            "token": "fake-jwt-token",
            "user": username
        }), 200

    return jsonify({
        "error": "Invalid username or password"
    }), 401


@app.route("/metrics", methods=["GET"])
def metrics():
    REQUEST_COUNT.inc()
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)