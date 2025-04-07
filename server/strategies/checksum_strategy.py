import hashlib
from abc import ABC, abstractmethod

class ChecksumStrategy(ABC):
    @abstractmethod
    def calculate(self, file_path: str) -> str:
        pass

# SHA256 strategija
class SHA256Checksum(ChecksumStrategy):
    def calculate(self, file_path: str) -> str:
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()

# MD5 strategija 
class MD5Checksum(ChecksumStrategy):
    def calculate(self, file_path: str) -> str:
        md5_hash = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                md5_hash.update(chunk)
        return md5_hash.hexdigest()
