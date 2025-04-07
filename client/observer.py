from abc import ABC, abstractmethod

class DownloadObserver(ABC):
    @abstractmethod
    def update(self, downloaded_bytes: int, total_bytes: int):
        pass


class ProgressPrinter(DownloadObserver):
    def update(self, downloaded_bytes: int, total_bytes: int):
        percent = (downloaded_bytes / total_bytes) * 100
        print(f"\rDownloaded: {downloaded_bytes} bytes ({percent:.2f}%)", end="", flush=True)


