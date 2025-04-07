from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse
from server.file_factory import FileFactory
from server.checksum_calculator import ChecksumCalculator
from server.strategies.checksum_strategy import SHA256Checksum, MD5Checksum

app = FastAPI()

@app.get("/file")
def get_file(
    algorithm: str = Query("sha256"),
    file_type: str = Query("bin")  
):
    try:
        file_path = FileFactory.create_temp_file(file_type=file_type)
    except ValueError as e:
        return {"error": str(e)}

    if algorithm.lower() == "sha256":
        strategy = SHA256Checksum()
    elif algorithm.lower() == "md5":
        strategy = MD5Checksum()
    else:
        return {"error": f"Unsupported algorithm: {algorithm}"}

    calculator = ChecksumCalculator()
    calculator.set_strategy(strategy)
    checksum = calculator.calculate(file_path)

    def file_streamer(file_path):
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                yield chunk
                #print(f"Sending chunk of size {len(chunk)} bytes")

    headers = {"X-Checksum": checksum}
    return StreamingResponse(file_streamer(file_path), media_type="application/octet-stream", headers=headers)

