import os
import sys
import json
from flask import Flask, jsonify, render_template

# Stop writing Object Code
sys.dont_write_bytecode = True

# Project Specific modules
from models import Model

# Init app
app = Flask(__name__)
db = Model("result_info.db")

@app.route('/')
def root():
    # return str(db.fetch())
    return render_template('index.html')

@app.route("/<roll>")
def search(roll):
    result = json.dumps([dict(row) for row in db.fetch(roll)][0])
    result = result[11:-2].replace('"', '')
    result = result.replace(', ', "\n")
    result = result.upper()
    return jsonify({"messages": [{"text": result}]})

# Run app
if __name__ == "__main__":
    app.debug = True
    app.port = int(os.environ.get("PORT", 5000))
    app.run()
    db.done()
