import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show, output_file
from bokeh.io import output_notebook, push_notebook
from ipywidgets import interact, FloatSlider
from copy import copy


dframe = pd.read_csv("datasets/cars.csv")
pricevdist = dframe[['odometer_value', 'price_usd']]

X = pricevdist['odometer_value'].to_numpy()[:200]
Y = pricevdist['price_usd'].to_numpy()[:200]

p = figure(width=600, height=400, x_axis_label="Mileage", y_axis_label="Price", title="Price vs Mileage", x_range=(0,500000), y_range=(0, 30000))
p.circle(X, Y, x=0, y=0)

p2 = figure(width=600, height=400, x_axis_label="Mileage", y_axis_label="Price", title="Price vs Mileage", x_range=(0,500000), y_range=(0, 30000))
p2.circle(X, Y, x=0, y=0)

x = np.linspace(0, 600000, 500)
y = 0.05*x
ref = p2.line(x, y)


p3 = figure(width=600, height=400, x_axis_label="Mileage", y_axis_label="Price", title="Price vs Mileage", x_range=(0,500000), y_range=(0, 30000))
p3.circle(X, Y, x=0, y=0)

x_p = np.linspace(0, 600000, 500)
y_p = 0.05*x_p - 0.0025*x_p**2 - 0.0003*x_p**3

ref2 = p3.line(x_p, y_p)



def show_price_vs_mileage(p=p):
    output_notebook()
    show(p)

def show_pvm_with_sliders(p=p2):
    output_notebook()
    show(p, notebook_handle=True)
    interact(update_graph, w=(-0.3, 0.3, 0.001), b=(-50000, 50000))

def update_graph(w=0.05, b=0):
    x = ref.data_source.data['x']
    ref.data_source.data['y'] = w * x + b
    push_notebook()

def show_poly(p=p3):
    output_notebook()
    show(p, notebook_handle=True)
    interact(update_graph_poly, 
            w1=FloatSlider(value=1e-3, min=-0.1, max=0.1, 
                    step=0.001, readout_format='.3f'), 
            w2=FloatSlider(value=0, min=-10, max=10, 
                    step=0.001, readout_format='.3f'), 
            w3=FloatSlider(value=0, min=-10, max=10, 
                    step=0.0001, readout_format='.5f'), 
            b=(-50000, 50000))

def update_graph_poly(w1=0.05, w2=-0.0025, w3=-0.0003, b=10000):
    x = ref2.data_source.data['x']
    ref2.data_source.data['y'] = w1*x + 1e-7*w2*x**2 + 1e-13*w3*x**3 + b
    push_notebook()