from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Konfiguration aus Umgebungsvariablen
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Datenbankmodell
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    done = db.Column(db.Boolean, default=False)

# Route zum Abrufen aller ToDos
@app.route("/todos", methods=["GET"])
def list_todos():
    todos = Todo.query.all()
    return jsonify([
        {"id": todo.id, "title": todo.title, "done": todo.done}
        for todo in todos
    ])

# Route zum Hinzufügen eines neuen ToDos
@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Bad Request, 'title' erforderlich"}), 400

    todo = Todo(title=data["title"])
    db.session.add(todo)
    db.session.commit()
    return jsonify({"id": todo.id, "title": todo.title, "done": todo.done}), 201

if __name__ == "__main__":
    # Stelle sicher, dass die Tabellen erstellt werden
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5000)