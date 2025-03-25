import flask


# TODO: change this to your academic email
AUTHOR = "avab@sas.upenn.edu"


app = flask.Flask(__name__)


# This is a simple route to test your server


@app.route("/")
def hello():
    return f"Hello from my Password Validator! &mdash; <tt>{AUTHOR}</tt>"


# This is a sample "password validator" endpoint
# It is not yet implemented, and will return HTTP 501 in all situations


@app.route("/v1/checkPassword", methods=["POST"])
def check_password():
    data = flask.request.get_json() or {}
    pw = data.get("password", "")

    # FIXME: to be implemented

    # Process password
    lengthCheck = False
    upperCheck = False
    digitCheck = False
    specialCheck = False
    count = 0
    for char in pw:
        count += 1
        if (char.isupper()):
            upperCheck = True
        if (char.isdigit()):
            digitCheck = True
        if (char in "!@#$%^&*"):
            specialCheck = True
    if (count < 8 ):
        lengthCheck = False
    
    # return result based on check
    if (not lengthCheck):
        return flask.jsonify({"valid": False, "reason": "Too short"}), 200
    elif (not upperCheck):
        return flask.jsonify({"valid": False, "reason": "No uppercase letter"}), 200
    elif (not digitCheck):
        return flask.jsonify({"valid": False, "reason": "No digit"}), 200
    elif (not specialCheck):
        return flask.jsonify({"valid": False, "reason": "No special character"}), 200
    else:
        return flask.jsonify({"valid": True, "reason": ""}), 200
