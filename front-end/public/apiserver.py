from flask import Flask, request, jsonify
import subprocess
from turtle import position
from rssi import RSSI_Localizer
import math
import time
from rout import position2


app = Flask(__name__)

@app.route('/position', methods=['GET'])
def load():
    return {"position":position2()}
      


if __name__ == "__main__":
        app.run(debug=True)