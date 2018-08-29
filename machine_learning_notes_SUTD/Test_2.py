from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import numpy as np

def linear_regression(file):

    data = open(file, 'r')
    list = data.readlines()

    time_list = []
    temp_list = []
    for i in list:
        point = i.strip().split(',')
        time = float(point[0])
        temp = float(point[1])
        time_list.append(time)
        temp_list.append(temp)
    time_list = np.array(time_list[:25])
    temp_list = np.array(temp_list[:25])
    Tamb = np.array([temp_list[0] for i in temp_list])
    if temp_list[3] >temp_list[0]:
        delta = 0.1
        tw = temp_list[-1]+0.1
    elif temp_list[3]<temp_list[0]:
        delta = -0.1
        tw = temp_list[-1]-0.1
    R_2 = 0
    while True:
        Tw = np.array([tw for i in temp_list])
        LN = np.log((temp_list - Tw) / (Tamb - Tw))
        x = time_list[:,np.newaxis]
        y = LN[:,np.newaxis]

        #x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=size, random_state=seed)

        regr = linear_model.LinearRegression()
        regr.fit(x, y)

        y_pred = regr.predict(x)
        New_R_2 = r2_score(y, y_pred)
        if New_R_2 > R_2:
            R_2 =New_R_2
            tw = tw +delta
        else:
            break
    return tw


file = 'data_54.8.txt'
print(linear_regression(file))