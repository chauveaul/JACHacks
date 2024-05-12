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
        
        drawimage(r1, r2, r3)
        # return drawimage(r1,r2,r3), 201
    return "yes", 200
      


if __name__ == "__main__":
        app.run(debug=True)