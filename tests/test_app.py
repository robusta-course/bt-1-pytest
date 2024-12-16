from app.app import app

def test_add():
    client = app.test_client()
    response = client.get('/add/2/4')
    assert response.status_code == 200
    assert b'{"result":7}' in response.data
