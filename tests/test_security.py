from http import HTTPStatus

from jwt import decode

from fast_zero.security import (
    ALGORITHM,
    SECRET_KEY,
    create_access_token,
)


def test_jwt():
    data = {'sub': 'test@test.com'}
    token = create_access_token(data)
    result = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    assert result['sub'] == data['sub']
    assert result['sub']


def test_jwt_invalid_token_exception(client, user):
    response = client.delete(
        '/users/1', headers={'Authorization': 'Bearer token-valido'}
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


# def test_jwt_invalid_credentials(client, user):
#    response = get_current_user(client, 'Bearer token-valido')
#    print(response)
#    # assert response.status_code == HTTPStatus.UNAUTHORIZED
