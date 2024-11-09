from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='test', email='testtest@test.com', password='testpass'
    )
    session.add(user)
    session.commit()
    result = session.scalar(
        select(User).where(User.email == 'testtest@test.com')
    )
    assert result.username == 'test'
