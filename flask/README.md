# Simple Flask HTTP API File Upload Server

## Usage:

### File Uploads:

2 things are necessary in the request:
* The key called "data" in the req body (The Value for the key is not yet validated)
* The basic key/value authentication field

```bash
curl -d "data=$(cat my_file.txt)" --user test:test http://<IP>:<PORT>/upload
```
The app will create a new file name containing a timestamp.
Upon confirmation we receive the file name (This will be required for downloading it in the future)

### File Downloads:

(examples)
```bash
curl --user test:test http://<ip>:<port>/files/my-file

wget --user test --password test http://<ip>:<port>/files/my-file
```
