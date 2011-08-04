"""Simple tests to check how nose-pynotify will work"""
def test_foo():
    assert 1==1

def test_failure():
    assert 2==1, "Sample failing test"

def test_error():
    1/0
