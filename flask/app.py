from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_httpauth import HTTPBasicAuth
from datetime import datetime

'''

Basic Flask HTTP API with basic authentication. Purpose:
    Upload files or data to this server

(Use dotenv for handling user/passwords instead of assigning variables)

'''

USERNAME = 'test'
PASSWORD = 'test'

app = Flask(__name__)
auth = HTTPBasicAuth()

@app.route('/upload', methods=['POST'])
@auth.login_required
def login():
    error = None
    if request.method == 'POST':
        file_info = []
        try:
            data = request.form.to_dict(flat=False)['data'][0]
            if len(data) > 0:
                timestamp = '{:%H%M%S-%Y%m%d}'.format(datetime.now())
                FILENAME = "upload-" + timestamp
                with open(FILENAME, 'w') as F:
                    F.write(data)
            return "[+] ok\n"
        except:
            return "[!] No data"

    else:
        return "[!] Only POST Requests allowed!"


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
