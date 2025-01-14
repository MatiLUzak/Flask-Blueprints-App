import requests

BASE_URL = "http://localhost:5000/api"

def test_get_data():
    response = requests.get(f"{BASE_URL}/data")
    assert response.status_code == 200, "Should be 200 when fetching data"
    data = response.json()
    assert isinstance(data, list), "Response JSON should be a list"

def test_post_data_success():
    new_point = {
        "feature1": 3.14,
        "feature2": 2.71,
        "category": 1
    }
    response = requests.post(f"{BASE_URL}/data", json=new_point)
    assert response.status_code == 200, "Should be 200 when adding a record"
    response_json = response.json()
    assert "id" in response_json, "'id' key should be in the response"
    record_id = response.json()["id"]
    requests.delete(f"{BASE_URL}/data/{record_id}")

def test_post_data_invalid():
    invalid_point = {
        "feature1": "invalid_value"
    }
    response = requests.post(f"{BASE_URL}/data", json=invalid_point)
    assert response.status_code == 400, "Should be 400 for invalid data"
    assert response.json() == {"error": "Invalid data"}, "Error should be 'Invalid data'"

def test_delete_data():
    new_point = {
        "feature1": 1.23,
        "feature2": 4.56,
        "category": 9
    }
    create_response = requests.post(f"{BASE_URL}/data", json=new_point)
    assert create_response.status_code == 200, "Should be 200 when creating a record"

    record_id = create_response.json()["id"]
    delete_response = requests.delete(f"{BASE_URL}/data/{record_id}")
    assert delete_response.status_code == 200, "Should be 200 when deleting a record"
    assert delete_response.json() == {"deleted_id": record_id}, "Response should confirm deleted record"

    second_delete_response = requests.delete(f"{BASE_URL}/data/{record_id}")
    assert second_delete_response.status_code == 404, "Should be 404 for non-existent record"
    assert second_delete_response.json() == {"error": "Record not found"}, "Error should be 'Record not found' for non-existent record"
