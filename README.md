# Topic 1 -- Linear Regression

## Overview of this Repository
This repository contains all the teaching material related to **Linear Regression**. The master `branch` contains the sample code for the instructor to **reference**, and the `workshop` branch contains the **empty notebooks** for the instructor and students to program in.

## For the Instructors:

This section details instructions to guide the instructor in delivering the course. The instructor should fill out the blank notebooks in the `workshop` branch according to the reference in the `master` branch (if it is possible, use dual monitors so you can have the reference code opened side by side.) **There will be function calls already written in the blank notebook, please run those calls without modifications.**

Below is the curriculum of this repository, as well as the order of content to be delivered. **Be sure to familiarize yourself with the code before teaching! Feel free to explore the notebooks as well as the web app `gpu-perf.py`**.

### Getting set up
1. Clone this repo into a working directory
2. Create and activate a virtual environment with the command below:
```bash
# MacOS/Linux
$ python3 -m venv env
$ source env/bin/activate
```
```bat
:: Windows
\> python -m venv env
\> .\env\Scripts\activate
```
3. If you are in the virtual environment, you should see the `(env)` marker. Now, install all the dependencies:
```bash
# MacOS/Linux
$ pip install -r requirements.txt
```
```bat
:: Windows
\> python -m pip install -r requirements.txt
```
4. You are ready to go! Both the course material notebook and the programming project are meant to be done on your local **jupyter notebook** (Colab doesn't support some dynamic notebook features).

## Topic 1 -- Linear Regression
#### The Gist of this section:
- A lot of the course material is contained in the textboxes of the notebook. Refer to those to give you an idea of what to talk about.
- When coding, commentate on your code, let the students know what it is about. Comments are in the reference code so you can quickly understand what that section of code is doing.

### What is Linear Regression
- Reference the text in the notebook on explaining what linear regression is
- Some functions are already there, please do not make any modifications to it. 
    - These functions are pre-defined functions in `disp_utils.py` and are used to display visuals.
    - **commentate on the visuals**
    - introduce the linear sum formula \(\hat{y} = wx + b\); There is a plot with sliders where you can change \(w\) and \(b\).
- Cost Function
    - Be sure to tell student that it is used to measure how bad the fit is
    - Don't get too in-detail with the math, simply let students know that **MSE** is the cost function used for linear regression problems.
- Gradient Descent
    - Let students know that when you plot a cost function, it will be shaped like a bowl (see visuals)
    - to get to the point of least error, you will go down the slope (gradient)

### Training a Linear Regression Model
- Start by giving a brief description of the modules 
- Loading and Visualizing the Dataset
    - `odometer_value` vs `price_usd`
    - In general, commentate on the code while you are coding
    - `train_test_split` -- if students ask why we need to split the data into a train/test set, give the students a full answer, but also inform them that this will be covered in detail in Topic 3
- Fitting the Linear Model
    - Continue commentating on the code while you code
    - > Note: This first model fits very poorly. This is because we are only fitting one variable to price, which is a multi-variable relation. **Allude to the next section**
- Observations
    - get the students to fill out the observations table

### Linear Regression with Multiple Variables
- Refer to the text while teaching
- Choose the features based on what you think correlates with the price.
    - choose features when its potentially too computationally expensive to use all the features
- Training 
    - Much of the same as before
- Observations
    - Make sure the students fill out the observations table

### Polynomial Regression
- Teach from the text in the notebook
    - be sure to describe the picture shown (note the non-linear nature of the curve)
- Get the students to play around with the sliders
- Train the model
    - Same process as before, except with the use of `PolynomialFeatures()`
- Observations
    - get students to write down observations

## gpu_perf_predictor_train.ipynb
#### The General Gist
- This is the notebook used to train a linear regression model used for the programming exercise
- there are comments written throughout the reference notebook to guide the instructor through
- commentate while coding so students understand what every line of code does
- MUST TALK ABOUT LEARNING RATE AND WHAT IT DOES
- Don't worry about explaining what batch normalization does, as it will be covered in a later topic


## gpu-perf.py
- This is the web server that is part of the programming exercise. Once you trained the model from `gpu_perf_predictor_train.ipynb`, you would load it here and run the server.
- Program from top to bottom, commentating on the code while writing. Your commentary should give students a thorough understanding of what each line does.



