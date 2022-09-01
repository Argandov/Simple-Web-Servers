from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_httpauth import HTTPBasicAuth
from datetime import datetime
from os.path import exists
import os

'''

Basic Flask HTTP API with basic authentication. Purpose:
    Upload files or data to this server

(Use dotenv for handling user/passwords instead of assigning variables)

'''
app = Flask(__name__)
auth = HTTPBasicAuth()

USERNAME = 'test'
PASSWORD = 'test'
app.config['UPLOAD_FOLDER'] = 'files'

@app.route('/upload', methods=['POST'])
@auth.login_required
def upload_file():
    error = None
    if request.method == 'POST':
        file_info = []
        try:
            data = request.form.to_dict(flat=False)['data'][0]
            if len(data) > 0:
                timestamp = '{:%H%M%S-%Y%m%d}'.format(datetime.now())
                FILE = "upload-" + timestamp
                FILENAME = app.config['UPLOAD_FOLDER'] + "/" + FILE
                with open(FILENAME, 'w') as F:
                    F.write(data)
                return f"[+] ok {FILE}\n"
            else:
                return f"[+] File {FILE} is empty"
        except:
            return "[!] Use data=$(some content) to send data"
    else:
        return "[!] Only POST requests accepted!"

@app.route('/files/<path:filename>', methods=['GET'])
@auth.login_required
def download_file(filename):
    _path = app.config['UPLOAD_FOLDER']
    Download = _path + "/" + filename
    if exists(Download):
        with open(Download) as F:
            return F.read()
    else:
        return "[404] File does not exist!"




@auth.verify_password
def authenticate(username, password):
	if username and password:
		if username == USERNAME and password == PASSWORD:
			return True
		else:
			return False
	return False

if __name__ == '__main__':
   app.run(debug = True)
