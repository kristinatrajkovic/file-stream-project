from server.strategies.checksum_strategy import ChecksumStrategy, SHA256Checksum

class ChecksumCalculator:
    _instance = None

    def __new__(cls, strategy: ChecksumStrategy = None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.strategy = strategy or SHA256Checksum()
        return cls._instance

    def calculate(self, file_path: str) -> str:
        return self.strategy.calculate(file_path)

    def set_strategy(self, strategy: ChecksumStrategy):
        self.strategy = strategy

