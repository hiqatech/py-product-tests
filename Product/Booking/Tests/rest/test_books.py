import requests


def test_get_book_by_id():
    url = "https://run.mocky.io/v3/9b2fc100-4c56-473d-b488-323dfd26396c/books/1"  # Replace with your mock API URL
    response = requests.get(url)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=UTF-8"

    data = response.json()
    assert isinstance(data, dict)
    assert "id" in data
    assert "title" in data
    assert "author" in data


def test_create_book():
    url = "https://run.mocky.io/v3/628dca34-286a-4850-902b-b5fdd89e0ce3/books"  # Replace with your mock API URL
    new_book = {"title": "The Hobbit", "author": "J.R.R. Tolkien"}
    response = requests.post(url, json=new_book)
    assert response.status_code == 201
    assert response.headers["Content-Type"] == "application/json; charset=UTF-8"

    data = response.json()
    assert "id" in data
    assert data["title"] == "The Hobbit"
    assert data["author"] == "J.R.R. Tolkien"


def test_update_book():
    url = "https://run.mocky.io/v3/..."  # Replace with mock API URL for updating a book
    book_id = 1  # Existing book ID to update
    updated_book = {"title": "The Lord of the Rings: The Fellowship of the Ring", "author": "J.R.R. Tolkien"}
    response = requests.put(url, json=updated_book)
    assert response.status_code == 200  # Or the appropriate code for your mock API
    assert response.headers["Content-Type"] == "application/json; charset=UTF-8"

    data = response.json()
    assert data["id"] == book_id
    assert data["title"] == updated_book["title"]
    assert data["author"] == updated_book["author"]


def test_delete_book():
    url = "https://run.mocky.io/v3/..."  # Replace with mock API URL for deleting a book
    book_id = 2  # ID of the book to delete
    response = requests.delete(url)
    assert response.status_code == 204  # 204 No Content signifies successful deletion
    assert response.text == ""  # Verify an empty response body