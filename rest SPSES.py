from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

nameScore = {}

class Statistik(Resource):
    def get(self, name):
        if name in nameScore:
            return {name: nameScore[name]}
        return {"Message" : "Nicht vorhanden"}

    def post(self, name):
        print(name)
        existing = name in nameScore
        d = request.get_json(force=True)
        nameScore[name] = {'playerWins': d['playerWins'], 'compWins':d['compWins'], 'stats': d['stats']}
        if existing:
            return {"Message" : "Überschrieben"}
        return {"Message" : "Neu hinzugefügt"}

api.add_resource(Statistik, '/stats/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)