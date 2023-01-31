import flask
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

nameScore = {}


@app.route("/")
def hello_world():
    return "hello world"


@app.route("/get", methods=['GET', 'POST'])
def get():
    r = request.get_json(force=True)
    if r["name"] in list(nameScore.keys()):
        return {r["name"]: nameScore[r["name"]]}
    #return flask.jsonify(nameScore)
    return {"Message": "Nicht vorhanden"}


@app.route("/post", methods=['POST'])
def put():
    r = request.get_json(force=True)
    print(r["name"])
    existing = r["name"] in list(nameScore.keys())
    d = r["statistic"]
    nameScore[r["name"]] = {'playerWins': d['Players-Wins'], 'compWins': d['Computers-Wins'], 'draw': d['Draw']}
    if existing:
        return flask.jsonify({"Message": "Überschrieben"})
    return flask.jsonify({"Message": "Neu hinzugefügt"})


if __name__ == '__main__':
    app.run(debug=True)
