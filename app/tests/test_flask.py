from flask import Flask, url_for
def test_api_response_code(client):
    res = client.get(url_for('cats'))
    assert res == 200

