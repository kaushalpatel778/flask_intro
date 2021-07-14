from flask import Flask,request
from operations import add,sub,mult,div
app= Flask(__name__)

# add
@app.route('/add')
def do_add():
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    result= add(a,b)
    return str(result)
#Subtract
@app.route('/sub')
def do_sub():
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    result= sub(a,b)
    return str(result)

#Multiply
@app.route("/mult")
def do_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)
    return str(result)

#Division
@app.route("/div")
def do_div():   
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = div(a, b)
    return str(result)


operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
    }    

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)