from flask import Flask, render_template, request, redirect,url_for
from com.kimyoungoncom.auth.login_controller import LoginController
from com.kimyoungoncom.calculator.bmi_controller import BmiController, BmiController
from com.kimyoungoncom.calculator.bmi_model import BmiModel
from com.kimyoungoncom.calculator.calc_model import CalcModel
from com.kimyoungoncom.calculator.calc_controller import CalcController
from com.kimyoungoncom.auth.login_model import LoginModel
from com.kimyoungoncom.calculator.gugudan_controller import GugudanController
from com.kimyoungoncom.calculator.gugudan_model import GugudanModel
from com.kimyoungoncom.grade.grade_controller import GradeController
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
    print("플러스페이지로 이동")   
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

@app.route('/discount', methods = ["POST","GET"])
def discount():
    print("할인율 계산")
    amount = request.form.get('amount')  
    print("👌amount:", amount)

    if request.method == "POST":
        print("🤦‍♀️POST 방식으로 전송된 데이터")
        
    return render_template("calculator/discount.html")


@app.route('/login',methods=["POST"]) 
def login():
    print("❤️전송된 데이터 방식:", request.method)

    username = request.form.get('username')  
    password = request.form.get('password') 
    print("🙌username:", username)
    print("👌password:", password)

    

    controller = LoginController(username, password)
    resp: LoginModel = controller.getResult()

    return redirect(url_for(resp.result))
   
@app.route('/calc', methods=["POST", "GET"])
def calc():
    print("❤️전송된 데이터 방식:", request.method)

    if request.method == "POST":
        print("🤦‍♀️POST 방식으로 전송된 데이터")
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        opcode = request.form.get("opcode")


        controller = CalcController(num1=num1 , opcode=opcode, num2=num2)
        resp: CalcModel = controller.getResult()

        render_html ='<h3>결과보기</h3>'
        render_html += f'{resp.num1} {resp.opcode} {resp.num2} = {resp.result}'
        
        return render_template("calculator/calc.html", 
                           render_html = render_html)
    else:
        return render_template("calculator/calc.html")
    
@app.route('/gugudan', methods = ["POST","GET"])
def gugudan():
    print("구구단 계산")

    if request.method == "POST":
        print("🤦‍♀️POST 방식으로 전송된 데이터")
        dan = request.form.get("dan")  

        controller = GugudanController(dan = dan)
        resp: GugudanModel = controller.getResult()
        for i in resp.result:
            print(i)

        render_html ='<h3>결과보기</h3>'
        for i in resp.result:
            render_html += i+"<br/>"
        
    
        return render_template("calculator/gugudan.html", render_html = render_html)        
    return render_template("calculator/gugudan.html")

@app.route('/bmi', methods=["POST", "GET"])
def bmi():
    print("❤️전송된 데이터 방식:", request.method)

    if request.method == "POST":
        print("🤦‍♀️POST 방식으로 전송된 데이터")
        height = request.form.get("height")
        weight = request.form.get("weight")
        
        controller = BmiController(height=height, weight=weight)
        resp: BmiModel = controller.getResult()

        render_html ='<h3>결과보기</h3>'
        render_html += f"{resp.height}cm {resp.weight}kg의 BMI는 {resp.result}"
        
        
        return render_template("calculator/bmi.html", 
                           render_html = render_html)
    else:
        print("🤦‍♀️GET 방식으로 전송된 데이터")
        return render_template("calculator/bmi.html")
    
@app.route('/grade', methods=["POST", "GET"])
def grade():
    print("❤️전송된 데이터 방식:", request.method)

    if request.method == "POST":
        print("🤦‍♀️POST 방식으로 전송된 데이터")
        name = request.form.get("name")
        korean = request.form.get("korean")
        english = request.form.get("english")
        math = request.form.get("math")
        society = request.form.get("society")
        science = request.form.get("science")
        
        controller = GradeController(name=name, korean=korean, english=english,
                                      math=math, society=society, science=science)
        resp = controller.getResult()
        
       
        render_html ='<h3>결과보기</h3>'
        render_html += f"{resp.name}님의 학점은 {resp.result}입니다."
        
        return render_template("grade/grade.html", 
                           render_html = render_html)
    else:
        print("🤦‍♀️GET 방식으로 전송된 데이터")
        return render_template("grade/grade.html")
    








if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)

   app.config['TEMPLATES_AUTO_RELOAD'] = True
    