import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show, output_file
from bokeh.io import output_notebook, push_notebook
from ipywidgets import interact
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
    

