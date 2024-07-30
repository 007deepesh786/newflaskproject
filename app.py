from flask import Flask,make_response,jsonify
from model import db
app = Flask(__name__)


@app.route('/helo')
def hello_world():  # put application's code here
    return 'New Hello World!'
@app.route('/api/products',methods = ['GET'])
def getAllProducts():  # put application's code here
    return make_response(jsonify({"products": db}), 200)


if __name__ == '__main__':
    app.run()
