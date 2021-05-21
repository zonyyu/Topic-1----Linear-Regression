from email import message
from flask import Flask, render_template, redirect, url_for, request, jsonify

app = Flask(__name__)



@app.route('/')
def home():
    return render_template("index.html")

@app.route('/test1', methods=['POST'])
def test1():
    pnode = request.form.get("pnode")
    area = request.form.get("area")
    trans = request.form.get("trans")

    print(pnode, area, trans)
    return jsonify({'pred' : '42'})

if __name__ == "__main__":
    app.run(debug=True)
 