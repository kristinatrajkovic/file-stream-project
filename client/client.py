import requests
from checksum_strategy import SHA256Checksum, MD5Checksum
from observer import ProgressPrinter

url = "http://127.0.0.1:8000/file?algorithm=sha256"  # ili md5
response = requests.get(url, stream=True)

file_path = "received_file.bin"
content_length = response.headers.get('Content-Length')
total_bytes = int(content_length) if content_length else None
downloaded_bytes = 0

observer = ProgressPrinter()

with open(file_path, "wb") as f:
    for chunk in response.iter_content(chunk_size=4096):
        if chunk:
            f.write(chunk)
            downloaded_bytes += len(chunk)
            if total_bytes:
                observer.update(downloaded_bytes, total_bytes)
            else:
                print(f"\rDownloaded: {downloaded_bytes} bytes", end="", flush=True)

print("\nDownload complete.")

server_checksum = response.headers.get("X-Checksum")

algorithm = url.split("algorithm=")[-1]
if algorithm == "sha256":
    strategy = SHA256Checksum()
elif algorithm == "md5":
    strategy = MD5Checksum()
else:
    print("Unsupported algorithm")
    exit()

checksum = strategy.calculate(file_path)
print(f"Checksum from server: {server_checksum}")
print(f"Checksum calculated:  {checksum}")

if checksum == server_checksum:
    print("Checksums match! File integrity verified.")
else:
    print("Checksums do not match!")

