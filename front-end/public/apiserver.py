from flask import Flask, request, jsonify
from rssi import RSSI_Localizer
from rout import position2
from triangulation import drawimage


app = Flask(__name__)

@app.route('/position', methods=['GET'])
def load():
    return {"position":position2()}

@app.route('/image', methods=['POST'])
def image():
    if request.is_json:
        country = request.get_json()
        r1 = country["r1"]
        r2 = country["r2"]
        r3 = country["r3"]
        r1=float(r1)
        r2=float(r2)
        r3=float(r3)
        return drawimage(r1,r2,r3), 201
    return {"error": "Request must be JSON"}, 415
      


if __name__ == "__main__":
        app.run(debug=True)