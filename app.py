import re

from flask import Flask, request, jsonify
from Model import run

app = Flask(__name__)


@app.route('/', methods=["POST"])
def getJava():
    input = request.form['text']
    result = run(input)
    result = re.sub('\s.\s<EOS>', '', result)
    result = result[1:]
    result = result.split(', ')
    response = {"java": result[0], "line": result[1]}
    return jsonify(response)


if __name__ == '__main__':
    app.run()
    exec('/Users/rene/Workspace/WPI/Artificial Intelligence/TranslationModelServer/Model.py')
