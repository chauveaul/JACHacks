from flask import Flask, request, jsonify
from rssi import RSSI_Localizer
from rout import position2
from triangulation import drawimage
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@cross_origin()

@app.route('/position', methods=['GET'])
def load():
    return {"position":position2()}

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@cross_origin()

@app.route('/image', methods=['POST'])
def image():
    if request.is_json:
        data = request.get_json()
        r1 = float(data["r1"])
        r2 = float(data["r2"])
        r3 = float(data["r3"])

        # Draw image based off points given
        # Does python have rest operator ex.(...data).
        # This grabs however many args are given and puts it in an array
        drawimage(r1, r2, r3)
    return "yes", 200

@app.route('/counter', methods=['POST'])
def counter():
    if request.is_json:
        data = request.get_json()
        counter = int(data["counter"])

if __name__ == "__main__":
        app.run(debug=True)
