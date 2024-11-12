from http import HTTPStatus

from jwt import decode

from fast_zero.security import create_access_token, settings


def test_jwt():
    data = {'sub': 'test@test.com'}
    token = create_access_token(data)
    result = decode(
        token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
    )
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
