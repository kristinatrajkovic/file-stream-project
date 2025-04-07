File Streaming with Checksum Verification
This project implements a file streaming system with checksum validation, ensuring file integrity. The
system consists of a server and a client. The server streams files to the client while calculating their
checksum using SHA256 or MD5 algorithms. The client receives the file, calculates the checksum,
and compares it with the server's checksum to ensure the integrity of the downloaded file.
## Features
- Stream files from the server to the client.
- Supports checksum algorithms (SHA256 and MD5) for integrity verification.
- Displays real-time download progress on the client.
- Verifies file integrity by comparing checksums.

## Installation
### Clone the repository:
To clone the repository to your local machine, use the following command:
```bash
git clone <repository_url>
cd file_stream_project
```
### Set up a virtual environment:
Create a virtual environment and activate it:
```bash
# For Windows
python -m venv venv
venv\Scripts\activate
# For Linux/macOS
python -m venv venv
source venv/bin/activate
```
### Install dependencies:
Install the required Python libraries by running the following command:
```bash
pip install -r requirements.txt
```
## Usage
### Run the Server:
The server is built with FastAPI and uses `uvicorn` as an ASGI server. To start the server, run the
following command:
```bash
uvicorn server.server:app --reload
```
The server will start and be accessible at `http://127.0.0.1:8000/`.

### Run the Client:
The client downloads the file from the server and verifies its checksum. To run the client, use:
```bash
python client/client.py
```
You can specify the checksum algorithm (either `sha256` or `md5`) when sending the request from
the client to the server.

### Example URL to download the file with the SHA256 checksum algorithm:
```bash
http://127.0.0.1:8000/file?algorithm=sha256
```
You can replace `sha256` with `md5` in the URL to use the MD5 checksum algorithm.

### Example Output:
The client will show a real-time display of the download progress, such as:
```
Downloaded: 10485760 bytes (1.00%)
Downloaded: 20971520 bytes (2.00%)
...
Downloaded: 104857600 bytes (100.00%)
Download complete.
Checksum from server: f7f3be3033be27738fe6a05085336a145efeac3cdc7926635b03de0d6d42fb2f
Checksum calculated: f7f3be3033be27738fe6a05085336a145efeac3cdc7926635b03de0d6d42fb2f
Checksums match! File integrity verified.
```
If the checksums match, the client will display `File integrity verified.` If they don't, it will print
`Checksums do not match!`.

## File Structure
### `server/`:
- **`server.py`**: FastAPI server code that streams files and calculates checksums.
- **`file_factory.py`**: Utility to generate temporary files of different types (binary, text, JSON).
- **`checksum_calculator.py`**: Contains classes for checksum calculation strategies (SHA256 and
MD5).
- **`observer.py`**: Implements the observer pattern for tracking download progress.
- **`strategies/`**: Contains checksum calculation strategies.
### `client/`:
- **`client.py`**: The client code for downloading files, calculating checksums, and verifying file
integrity.

## Contributing
If you'd like to contribute to this project, please feel free to fork the repository and submit a pull
request. You can also open an issue if you encounter any bugs or have feature requests.

### Steps to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to your fork (`git push origin feature/your-feature`).
5. Create a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Requirements
The following Python libraries are required to run this project:
- **`fastapi`**: FastAPI framework to build the server.
- **`uvicorn`**: ASGI server for FastAPI.
- **`requests`**: To send HTTP requests from the client.
To install the required libraries, run:
```bash
pip install -r requirements.txt
```