# Simple Flask HTTP API File Upload Server

Usage:

2 things are necessary in the request:
The key called "data" in the req body (The Value for the key is not yet validated)
The basic key/value authentication field

```bash
curl -d "data=$(cat my_file.txt)" --user test:test http://<IP>:<PORT>/upload
```
