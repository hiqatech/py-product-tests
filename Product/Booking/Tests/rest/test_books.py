import requests

url = "https://jsonplaceholder.typicode.com/todos"
header_exp = "application/json; charset=utf-8"

def test_get_tasks_by_id():
    task_id = "1"
    response = requests.get(url + "/" + task_id)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == header_exp
    data = response.json()
    print(data)
    assert isinstance(data, dict)
    assert "id" in data
    assert "title" in data
    assert "completed" in data


def test_create_task():
    new_task = {"title": "PyTest REST", "completed": "false"}
    response = requests.post(url, json=new_task)
    assert response.status_code == 201
    assert response.headers["Content-Type"] == header_exp
    data = response.json()
    print(data)
    assert "id" in data
    assert data["title"] == "PyTest REST"
    assert data["completed"] == "false"


def test_update_task():
    task_id = "4"
    updated_task = {"title": "PyTest REST", "completed": "true"}
    response = requests.put(url + "/" + task_id, json=updated_task)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == header_exp
    data = response.json()
    print(data)
    assert data["id"] == int(task_id)
    assert data["title"] == updated_task["title"]
    assert data["completed"] == updated_task["completed"]


def test_delete_task():
    book_id = "201"  # ID of the book to delete
    response = requests.delete(url + "/" + book_id)
    assert response.status_code == 200
    assert response.text == "{}"