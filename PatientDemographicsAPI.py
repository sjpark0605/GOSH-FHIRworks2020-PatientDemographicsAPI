from flask import Flask, jsonify, request, render_template
from DemographicsUtility import constructTargetGraph, constructTargetJson

possibleSelection = ["language", "gender", "year_group", "marital", "country", "distribution", "cumulative"]

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('Demonstrator.html')
        
@app.route('/demographics/graph', methods=['GET'])
def fetchDemoGraph():
    category = request.args.get('category')

    if (category in possibleSelection):
        return constructTargetGraph(category), 200

    return "Error: Invalid Data Type Request", 500

@app.route('/demographics/csv', methods=['GET'])
def fetchDemoCSV():
    category = request.args.get('category')

    if (category in possibleSelection):
        return constructTargetJson(category), 200

    return "Error: Invalid Data Type Request", 500

if __name__ == '__main__':
    app.run(debug=True, port="8910")