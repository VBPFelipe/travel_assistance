# /index.py
from flask import Flask, request, jsonify, render_template, make_response
import os
# import dialogflow
import requests
import json
# import pusher

app = Flask(__name__)

@app.route('/json', methods=['POST'])
def json_example():

    # validate the request body contains JSON
    if request.is_json:

        # Parse the JSON into a Python dictionary
        req = request.get_json()

        response_body = {
            "message" : "JSON received!",
            "sender"  : req.get("name")
        }

        res = make_response(jsonify(response_body), 200)

        # Returns a string along with an HTTP Request Status Code
        return res
    
    else:

        # The Request body wasn't JSON so return a 400 HTTP status code 
        return make_response(
            jsonify(
                {"message" : "Request body must be JSON"}
                ), 400)

@app.route('/read', methods=['GET'])
def read_json():
    return "oinpepê!"

# run Flask app
if __name__ == "__main__":
    app.run()    