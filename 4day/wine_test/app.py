from flask import Flask, render_template, request
from service import Service
serv = Service()

app = Flask(__name__)  #웹 어플리케이션

@app.route('/')  # 요청 url 등록
def root():
    return render_template('index.html')

@app.route('/wine-form')  # 요청 url 등록
def form():
    return render_template('form.html')

@app.route('/wine-test', methods=['POST'])  # 요청 url 등록
def test1():
    data=[]
    data.append(float(request.form['x1']))
    data.append(float(request.form['x2']))
    data.append(float(request.form['x3']))
    data.append(float(request.form['x4']))
    data.append(float(request.form['x5']))
    data.append(float(request.form['x6']))
    data.append(float(request.form['x7']))
    data.append(float(request.form['x8']))
    data.append(float(request.form['x9']))
    data.append(float(request.form['x10']))
    data.append(float(request.form['x11']))
    level = serv.wine_test(data)
    print(level)
    return render_template('index.html', level=level)

if __name__=='__main__':
    app.run()
