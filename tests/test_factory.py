from simple_app import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True, 'WTF_CSRF_ENABLED': False}).testing
