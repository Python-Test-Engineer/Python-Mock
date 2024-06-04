class Prod(object):
    def __init__(self):
        self.database = "prod.db"

    def get_connection(self):
        return f"connection: {self.database}"


class MockProd(object):
    def __init__(self):
        self.database = "mock.db"

    def get_connection(self):
        return f"connection: {self.database}"


def test_connection():
    obj = Prod()
    assert obj.get_connection() == "connection: prod.db"
    mock = MockProd()
    assert mock.get_connection() == "connection: mock.db"
