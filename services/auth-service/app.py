from flask import Flask, request, jsonify

app = Flask(__name__)

SERVICE_NAME = "auth-service"


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)