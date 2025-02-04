from flask import Flask, render_template, request, redirect,url_for
app = Flask(__name__)

@app.route('/')
def intro():   
    return render_template("auth/login.html")

@app.route('/home')
def home():
    print("홈페이지로 이동")   
    return render_template("index.html")

@app.route('/plus')
def plus():   
    print("플러스페이지지로 이동")   
    return render_template("calculator/plus.html")


@app.route('/minus')
def minus():   
    print("홈페이지로 이동")   
    return render_template("calculator/minus.html")

@app.route('/multiple')
def multiple():   
    print("홈페이지로 이동")   
    return render_template("calculator/multiple.html")

@app.route('/divide')
def divide():   
    print("홈페이지로 이동")   
    return render_template("calculator/divide.html")

@app.route('/finance')
def finance():   
    return render_template("esg/esg_chatbot/finance.html")

@app.route('/manufacture')
def manufacture():   
    return render_template("esg/esg_chatbot/manufacture.html")

@app.route('/retailer')
def retailer():   
    return render_template("esg/esg_chatbot/retailer.html")

@app.route('/esg_energy_date')
def esg_energy_date():   
    return render_template("esg/esg_platform/esg_energy_date.html")

@app.route('/esg_factory_automation')
def esg_factory_automation():   
    return render_template("esg/esg_platform/esg_factory_automation.html")

@app.route('/esg_finance_dashboard')
def esg_finance_dashboard():   
    return render_template("esg/esg_platform/esg_finance_dashboard.html")

@app.route('/esg_construction_reports')
def esg_construction_reports():   
    return render_template("esg/esg_system/esg_construction_reports.html")

@app.route('/esg_health_fin_qna')
def esg_health_fin_qna():   
    return render_template("esg/esg_system/esg_health_fin_qna.html")

@app.route('/retail_finance_automation')
def retail_finance_automation():   
    return render_template("esg/esg_system/retail_finance_automation.html")

@app.route('/fail')
def fail():   
    return render_template("auth/login.fail.html")



@app.route('/login',methods=["POST"])
def login():
    print("로그인 알고리즘")
    username = request.form.get('username')
    password = request.form.get('password')
    print("🙌username:", username)
    print("👌password:", password)
    if username =="kim" and password == '1234':
        print("😊로그인 성공")
        return redirect(url_for("home"))
    else:   
        print("😒로그인 실패")
        return render_template("auth/login.fail.html")
    
@app.route('/calc', methods=["POST", "GET"])
def calc():
    print("❤️전송된 데이터 방식:", request.method)

    

    if request.method == "POST":
        print("🤦‍♀️POST 방식으로 전송된 데이터")
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        opcode= request.form.get("opcode")
        print("👌num1:", num1)
        print("😍num2:", num2)
        print("➕opcode:", opcode)
        if opcode == "+":
            num3 = int(num1) + int(num2)
        elif opcode == "-":
            num3 = int(num1) - int(num2)
        elif opcode == "/":
            num3 = int(num1) / int(num2)
        else:
            num3 = int(num1) * int(num2)

        print(f"{num1} {opcode} {num2} = {num3}")
        print("👍계산 성공👍")
        return render_template("calculator/calc.html", num1 = num1, opcode = opcode, num2 = num2, num3 = num3)
    else:
        return render_template("calculator/calc.html")




if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)

   app.config['TEMPLATES_AUTO_RELOAD'] = True