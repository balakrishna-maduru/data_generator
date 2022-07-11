class _Config:
    shares_data = {}

    def __init__(self) -> None:
        self.__dict__ = self.shares_data
        self.record_count = 1
        self.round = 2
        self.low = 0
        self.high = 999

    def __str__(self) -> str:
        print(dir(_Config))
        return f"{self.shares_data}"

class Config(_Config):

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.shares_data.update(kwargs)


if __name__ == "__main__":
    c = Config()
    c1 = Config()
    print(c.record_count)
    c1.record_count = 2
    print(c.record_count)
    print(c1.record_count)
    c.record_count = 5
    print(c.record_count)
    print(c1.record_count)
