from flask import Flask
import database as db

app = Flask(__name__)

@app.route('/users/<email>')
def fetch(email):
    data = db.lookup_email(email)

    if data == 404:
        return("Error: 404 not found")
    else:
        return str(data[3])

if __name__ == '__main__':
    app.run(port=2424,debug=True,host="0.0.0.0")