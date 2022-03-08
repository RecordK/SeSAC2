import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


class Service:
    def wine_test(self, data: list):
        model = joblib.load('static/winequality_model.pkl')
        input = np.array([data])
        pred = model.predict(input)
        return pred

    def select(self):
        X_train = pd.read_csv('static/X_train.csv')
        X_test = pd.read_csv('static/X_test.csv')
        x_data = X_train.append(X_test)
        x_data = x_data.iloc[:, 1:]
        brand = x_data['brand'].unique().tolist()
        model = x_data['model'].unique().tolist()
        transmission = x_data['transmission'].unique().tolist()
        fuelType = x_data['fuelType'].unique().tolist()
        li = [brand, model, 0, transmission, 0, fuelType]
        return li

    def car_test(self, data: list, feature: list):
        model = joblib.load('static/car_model.pkl')
        data = pd.DataFrame(data).T
        data.columns = feature
        X_train = pd.read_csv('static/X_train.csv')
        X_test = pd.read_csv('static/X_test.csv')
        x_data = X_train.append(X_test)
        x_data = x_data.iloc[:, 1:]
        ex = x_data.append(data)

        ex["year"] = pd.to_numeric(ex["year"])
        ex["mileage"] = pd.to_numeric(ex["mileage"])
        ex["tax"] = pd.to_numeric(ex["tax"])
        ex["mpg"] = pd.to_numeric(ex["mpg"])
        ex["engineSize"] = pd.to_numeric(ex["engineSize"])
        ex = pd.get_dummies(ex)
        rd = ex[-1:]
        scaler = StandardScaler()
        rd = scaler.fit_transform(rd)
        pred = model.predict(rd)
        return pred
