from joke import get_joke_creator
from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class joke_resouce(Resource):

    def get(self):
        joke_creator = get_joke_creator()
        joke_of_the_day = joke_creator.create_joke()
        return jsonify({"joke_of_the_day": joke_of_the_day})

api.add_resource(joke_resouce, '/joke_of_the_day')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
