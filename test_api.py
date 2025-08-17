import requests


def test_yaml():
    resp = requests.get('')
    assert resp.status_code == 200