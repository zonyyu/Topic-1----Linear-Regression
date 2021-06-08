from email import message
from flask import Flask, render_template, redirect, url_for, request, jsonify






app = Flask(__name__)



@app.route('/')
def home():
    return render_template("index.html")

@app.route('/test1', methods=['POST'])
def test1():
    pnode = request.form.get("pnode") # Fab
    area = request.form.get("area") # Die Size
    trans = request.form.get("trans") # Millions Transistors
    mem = request.form.get("mem") # Memory Size





    #.item() gets the value in the torch.tensor
    return jsonify({'pred' : "GFLOPS: " + str(None)})

if __name__ == "__main__":
    app.run(debug=True)
 