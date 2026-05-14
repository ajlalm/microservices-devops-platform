from flask import Flask, jsonify, request

app = Flask(__name__)

SERVICE_NAME = "task-service"

tasks = [
    {"id": 1, "title": "Learn Docker", "completed": False},
    {"id": 2, "title": "Build Microservices Project", "completed": False}
]


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "service": SERVICE_NAME,
        "status": "healthy"
    }), 200


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({
        "service": SERVICE_NAME,
        "tasks": tasks
    }), 200


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({
            "error": "Task title is required"
        }), 400

    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "completed": False
    }

    tasks.append(new_task)

    return jsonify({
        "message": "Task created",
        "task": new_task
    }), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)