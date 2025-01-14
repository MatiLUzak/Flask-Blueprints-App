import requests

BASE_URL = "http://localhost:5000/api"

def test_get_data():

    response = requests.get(f"{BASE_URL}/data")
    assert response.status_code == 200, "Oczekiwano kodu 200 przy pobraniu danych"
    data = response.json()
    assert isinstance(data, list), "Oczekiwano listy danych w odpowiedzi JSON"

def test_post_data_success():

    new_point = {
        "feature1": 3.14,
        "feature2": 2.71,
        "category": 1
    }
    response = requests.post(f"{BASE_URL}/data", json=new_point)
    assert response.status_code == 200, "Oczekiwano kodu 200 przy poprawnym dodaniu rekordu"
    response_json = response.json()
    assert "id" in response_json, "W odpowiedzi powinien znajdować się klucz 'id' nowo utworzonego rekordu"

def test_post_data_invalid():
    invalid_point = {
        "feature1": "niepoprawna_wartosc"
    }
    response = requests.post(f"{BASE_URL}/data", json=invalid_point)
    assert response.status_code == 400, "Oczekiwano kodu 400 przy niepoprawnych danych"
    assert response.json() == {"error": "Invalid data"}, "Oczekiwano komunikatu o błędzie 'Invalid data'"

def test_delete_data():
    new_point = {
        "feature1": 1.23,
        "feature2": 4.56,
        "category": 9
    }
    create_response = requests.post(f"{BASE_URL}/data", json=new_point)
    assert create_response.status_code == 200, "Oczekiwano kodu 200 przy tworzeniu rekordu"

    record_id = create_response.json()["id"]
    delete_response = requests.delete(f"{BASE_URL}/data/{record_id}")
    assert delete_response.status_code == 200, "Oczekiwano kodu 200 przy poprawnym usunięciu rekordu"
    assert delete_response.json() == {"deleted_id": record_id}, "Oczekiwano potwierdzenia usuniętego rekordu"

    second_delete_response = requests.delete(f"{BASE_URL}/data/{record_id}")
    assert second_delete_response.status_code == 404, "Oczekiwano kodu 404 dla nieistniejącego rekordu"
    assert second_delete_response.json() == {"error": "Record not found"}, \
        "Oczekiwano komunikatu 'Record not found' przy próbie usunięcia nieistniejącego rekordu"
