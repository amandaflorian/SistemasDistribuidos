#Amanda Florian - 590673
#Rafael Pereira - 587761


from flask import Flask, jsonify, request
import json

app = Flask(__name__)

arrayMessages = []

@app.route('/',)
def getMessages():
    global arrayMessages
    return jsonify(arrayMessages)

@app.route('/inserir', methods=["POST"])
def postMessages():
    global arrayMessages
    print(request.json)
    arrayMessages.append(request.json)
    record = json.loads(request.data)
    return jsonify(record)

app.run()