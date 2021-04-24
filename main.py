
from flask import Flask, request, jsonify

from weka_extract_translate import WekaOutputExtractor

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/weka/<string:fileName>' , methods=['POST'])
def wekoutput(fileName):
    content = request.data
    extractor = WekaOutputExtractor()
    parsed_data = extractor.parseMetrics(fileName, content,'amahmoo6-adaboost_decision_stump-10-FIT')
    return parsed_data

