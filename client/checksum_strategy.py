import hashlib
from abc import ABC, abstractmethod

class ChecksumStrategy(ABC):
    @abstractmethod
    def calculate(self, file_path: str) -> str:
        pass

class SHA256Checksum(ChecksumStrategy):
    def calculate(self, file_path: str) -> str:
        sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()

class MD5Checksum(ChecksumStrategy):
    def calculate(self, file_path: str) -> str:
        md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                md5.update(chunk)
        return md5.hexdigest()

        