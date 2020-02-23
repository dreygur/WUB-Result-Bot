import os
import sys
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
    return jsonify({"messages": {"0": {"text": [dict(row) for row in db.fetch(roll)]}}})

# Run app
if __name__ == "__main__":
    app.port = int(os.environ.get('PORT', 5000))
    app.run(debug=True)
    db.done()
