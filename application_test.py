import application


def test_index():
    application.application.testing = True
    client = application.application.test_client()

    r = client.get("/")
    assert r.status_code == 200
    assert "Hello World" in r.data.decode("utf-8")
