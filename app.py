from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def login():   
    return render_template("auth/login.html")

@app.route('/home')
def home():   
    return render_template("index.html")

@app.route('/plus')
def plus():   
    return render_template("calculator/plus.html")


@app.route('/minus')
def minus():   
    return render_template("calculator/minus.html")

@app.route('/multiple')
def multiple():   
    return render_template("calculator/multiple.html")

@app.route('/devide')
def devide():   
    return render_template("calculator/devide.html")

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





if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)