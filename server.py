from flask import Flask, request
import os
import argparse

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-p", "--port", help="port serv", required=True)
parser.add_argument("-f", "--folder", help="Folder of save uploads")
args = parser.parse_args()

UPLOAD_FOLDER = args.folder

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/exf", methods=['GET','POST'])
def upload():
    if request.method == "POST":
        if 'file' not in request.files:
            return 'no file part'
        file = request.files["file"]
        if file.filename == "":
            return 'no selected file'
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(f"[+] File saved in {app.config['UPLOAD_FOLDER']}/{filename}")
            return 'ok'

    # Se for GET, exibe o formulário
    return '''
        <h1>ExfilServer</h1>
        <p>by @ph0r3nsic</p>
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
    '''

if __name__ == '__main__':
	app.run(host="0.0.0.0",port=int(args.port))