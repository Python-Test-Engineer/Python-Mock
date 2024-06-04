class Prod:
    def __init__(self):
        self.database = "prod.db"

    def get_connection(self):
        return f"connection: {self.database}"


class MockProd:
    call_count = 0

    def __init__(self):
        self.database = "mock.db"

    def get_connection(self):
        MockProd.call_count += 1
        return f"connection: {self.database}"

    @classmethod
    def called_how_may_times(cls):
        return cls.call_count


def test_connection():
    obj = Prod()
    assert obj.get_connection() == "connection: prod.db"
    mock = MockProd()
    assert mock.get_connection() == "connection: mock.db"
    assert MockProd.called_how_may_times() == 1
    N = 5
    for _ in range(N):
        mock.get_connection()
    assert MockProd.called_how_may_times() == N + 1  # 1 + 5 = 6
