import os
import tempfile
import random

class FileFactory:
    @staticmethod
    def create_temp_file(file_type="bin", size_in_mb=10):
        temp_file = tempfile.NamedTemporaryFile(delete=False)

        if file_type == "bin":
            with open(temp_file.name, 'wb') as f:
                f.write(os.urandom(size_in_mb * 1024 * 1024))  # Random binarni podaci

        elif file_type == "txt":
            text_data = "\n".join(["Random text line " + str(i) for i in range(1000)])
            with open(temp_file.name, 'w', encoding="utf-8") as f:
                f.write(text_data)

        elif file_type == "json":
            json_data = [{"id": i, "value": random.randint(1, 100)} for i in range(100)]
            with open(temp_file.name, 'w', encoding="utf-8") as f:
                json.dump(json_data, f, indent=4)

        else:
            raise ValueError(f"Unsupported file type: {file_type}")

        return temp_file.name


