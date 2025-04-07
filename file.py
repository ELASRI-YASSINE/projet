from flask import Flask
file = Flask(__name__)
@file.route("/")
def fonction():
     return " hello guys , I'm yassine student Cloud & Devops"
if __name__ == '__main__' :
      file.run(host="0.0.0.0", port=8080, debug=True)


