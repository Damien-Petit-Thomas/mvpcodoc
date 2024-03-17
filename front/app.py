from flask import Flask, render_template, request, jsonify, redirect
import requests
import os


def get_back_url():
    return os.environ.get("BACKEND_URL", "http://localhost:5000")


app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")



@app.route("/key", methods=["GET"])
def get_public_key():
    
    return requests.get(get_back_url() + "/key").json()


@app.route("/decode", methods=["GET"])
def decode_message():
    encoded_message = request.args.get("msg")
    print(encoded_message)
    if encoded_message is None:
        return "Missing message parameter", 400
    # return   print(encoded_message)
    return requests.get(get_back_url() + "/decode", params={"msg": encoded_message}).json()

@app.route("/health", methods=["GET"])
def health_check():
    return ""





if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)