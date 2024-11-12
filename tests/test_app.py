from http import HTTPStatus


def test_read_root_must_return_OK(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá mundo!'}
