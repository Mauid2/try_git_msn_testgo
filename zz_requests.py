import requests

resp=requests.get(
    "https://www.baidu.com",
    headers={},
    cookies={},
    params={},
    data={},
    json={},
    files={}
)
print(resp.text)
print(resp.status_code)
print(resp.headers)
print(resp.cookies)

assert resp.status_code == 200
assert "success" == resp.json()["state"]