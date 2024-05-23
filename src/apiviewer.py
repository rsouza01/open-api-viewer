from flask import Flask, render_template, Response, jsonify, request
import flask 
from flask import Flask, request, jsonify
from flask import Blueprint
from flasgger import Swagger, LazyJSONEncoder, swag_from

import swagger_config

app = Flask(__name__)
app.json_encoder = LazyJSONEncoder

swagger = Swagger(app, template=swagger_config.swagger_template,config=swagger_config.swagger_config)


#####################################################################################################
@swag_from("../docs/example.yaml" )
@app.route("/hello_world")
def hello_world():
    return "Hello, World!"


if __name__ == '__main__':
    print("* Starting Flask server...") 
    app.run(host='0.0.0.0', threaded=True, port=5000 , debug=False)