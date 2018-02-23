from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
	import systeminfo.systeminfo as si
	return si.systeminfo()

if __name__ == "__main__":
	app.run()
