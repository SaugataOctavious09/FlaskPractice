from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Hi, This is Saugata."

@app.route('/cal',methods=["GET"])
def math_op():
    operation = request.json["operation"]
    num1 = request.json["num1"]
    num2 = request.json["num2"]
    
    if operation == "add":
        result = num1 + num2
    elif operation == "mul":
        result = num1 * num2
    elif operation == "div":
        result = num1/num2
    else:
        result = num1 - num2
    return result
    
    
    
    

print(__name__)

if __name__ == '__main__':
    app.run()