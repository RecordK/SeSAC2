from flask import Flask, render_template, request
from service import Service
import pandas as pd

serv = Service()

# 플라스크 객체 생성
app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/car-test', methods=['POST'])
def test1():
    data = []
    for i in range(9):
        data.append(request.form['x{}'.format(i)])
    feature = ['brand', 'model', 'year', 'transmission', 'mileage', 'fuelType', 'tax', 'mpg', 'engineSize']
    levels = serv.car_test(data, feature)
    print(levels)
    return render_template('index.html', levels=levels)


@app.route('/car-form')  # 요청 url 등록
def carform():
    feature = ['brand', 'model', 'year', 'transmission', 'mileage', 'fuelType', 'tax', 'mpg', 'engineSize']
    li = serv.select()
    selfeature = [0, 1, 3, 5]
    k = [i for i in range(4)]
    return render_template('car-form.html', enumerate=enumerate, feature=feature, li=li, selfeature=selfeature, k=k)


@app.route('/wine-test', methods=['POST'])
def test2():
    data = []
    for i in range(1, 12):
        data.append(float(request.form['x{}'.format(i)]))
    level = serv.wine_test(data)
    print(level)
    return render_template('index.html', level=level)


@app.route('/wine-form')  # 요청 url 등록
def form():
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)  # flask 서버 실행
