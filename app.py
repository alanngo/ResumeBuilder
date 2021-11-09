import os
from flask import *
from buildResume.Color import *
from buildResume.Paper import *
from flask_cors import *
from helper.requests import *
from buildResume.ResumeBuilder import ResumeBuilder

from util.error_advice import *
from util.file_util import *

app = Flask(__name__)
app.register_blueprint(advice)
CORS(app) # lets other programs consume app

@app.route('/', methods=[GET])
def index():
    return "hello world"

@app.route('/sendFile', methods=[GET])
def download_file():
    return send_file("./sample.pdf", attachment_filename="sampleResume.pdf")

@app.route('/buildResume/<firstname>/<lastname>', methods=[POST, PUT])
def build_resume(firstname, lastname):
    clean_pdf("./")
    file_title =f"{firstname}{lastname}.pdf"
    body=request.get_json()
    resume = ResumeBuilder(
        file_title=file_title,
        header_color=RED, 
        category_color=BLACK, 
        list_color=GREY )
    resume.intro(
        name=f"{firstname} {lastname}",
        email=body["email"] or "spongebob@krustykrab.org",
        phone=str(body["phone"] or 1234567890),
        x=HEADER_POS,
        y=770)
    resume.save()
    return send_file(f"./{file_title}", attachment_filename=file_title)


if __name__ == '__main__':
    app.run(debug=True)