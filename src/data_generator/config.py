class _Config:
    shares_data = {}

    def __init__(self) -> None:
        self.__dict__ = self.shares_data
        self.record_count = 1
        self.round = 2
        self.low = 0
        self.high = 999

    def __str__(self) -> str:
        return f"{self.shares_data}"

class Config(_Config):

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.shares_data.update(kwargs)
