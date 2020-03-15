from flask import Flask
from flask import jsonify
import corona
app = Flask(__name__)
@app.route('/total', methods=['GET'])
def tot():
    return jsonify(corona.f)
@app.route('/', methods=['GET'])
def index():
    return jsonify(corona.d)
if __name__=="__main__":
    app.run(threaded=True, port=5000)
