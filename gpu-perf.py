from email import message
from flask import Flask, render_template, redirect, url_for, request, jsonify

import numpy as np
import import_ipynb
from gpu_perf_predictor_train import Linreg_p
import torch
from torch.autograd import Variable
from sklearn.preprocessing import PolynomialFeatures

gpu_model = Linreg_p(35, 1)
gpu_model.load_state_dict(torch.load("gpu-predictor.pt"))
gpu_model.eval()


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

    inputs = np.array([trans, area, mem, pnode]).reshape(1, 4)
    poly = PolynomialFeatures(degree=3)
    inputs_p = poly.fit_transform(inputs)

    torch_input = Variable(torch.from_numpy(inputs_p)).float()

    gflops = gpu_model(torch_input)
    
    return jsonify({'pred' : "GFLOPS: " + str(gflops.item())})

if __name__ == "__main__":
    app.run(debug=True)
 