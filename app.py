from flask import *
from flask_cors import *

app = Flask(__name__)
CORS(app) # lets other programs consume app

@app.route('/', methods=['GET'])
def index():
    return "hello world"

@app.route('/sendFile', methods=["GET"])
def download_file():
    return send_file("./sample.pdf", attachment_filename="sampleResume.pdf")

if __name__ == '__main__':
    app.run(debug=True)