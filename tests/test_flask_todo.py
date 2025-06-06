from flask_todo import app


def test_get_todos():
    with app.test_client() as client:
        response = client.get("/todos")
        assert response.status_code == 200
        assert isinstance(response.get_json(), list)
