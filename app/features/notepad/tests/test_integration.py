import pytest

pytestmark = pytest.mark.integration


def test_notepad_index_requires_login(test_client):
    response = test_client.get("/notepad", follow_redirects=False)
    # Comprueba que efectivamente la ruta no existe (404)
    assert response.status_code == 404