def test(client):
    """This should be my first test"""

    rv = client.get('/')
    assert b'Hello, Docker!' in rv.data
