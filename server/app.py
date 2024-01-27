#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(f"{parameter}")
    return f"{parameter}"

@app.route('/count/<int:num>')
def count(num):
    num_list = ""

    for i in range(num):
        num_list = num_list + f"{i}\n"

    return num_list

@app.route('/math/<num>/<operation>/<num2>')
def math(num, operation, num2):
    try:
        num = int(num)
        num2 = int(num2)
        operation = str(operation)
    except Exception as error:
        print("An Error Has Occurred: ", error)

    if operation == "+":
        return f"{num+num2}"
    elif operation == "-":
        return f"{num-num2}"
    elif operation == "*":
        return f"{num*num2}"
    elif operation == "div":
        return f"{num/num2}"
    elif operation == "%":
        return f"{num%num2}"
    else:
        return "Invalid Operation. Operation Must Be The Following: +, -, *, div, or %"




