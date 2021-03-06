import numpy as np
import matplotlib.pyplot as plt

# 벡터 x에 대해서 예측값 리턴
def prediction(theta_0, theta_1, x):
    return theta_0 + theta_1 * x

# 예측값과 목표 변수의 오차 리턴
def prediction_difference(theta_0, theta_1, x, y):
    return prediction(theta_0, theta_1, x) - y
    
# 경사 하강법 함수    
def gradient_descent(theta_0, theta_1, x, y, iterations, alpha):
    m = len(x)
    cost_list = []
    
    for _ in range(iterations):  # 정해진 번만큼 경사 하강을 한다
        error = prediction_difference(theta_0, theta_1, x, y)  # 오차 값
        cost = (error@error) / 2*m  # 손실 함수
        cost_list.append(cost)

        theta_0 = theta_0 - alpha * error.mean()
        theta_1 = theta_1 - alpha * (error * x).mean()

        if _ % 10 == 0:  # 10번 경사 하강할 때마다 그래프 그리기
            plt.scatter(house_size, house_price)
            plt.plot(house_size, prediction(theta_0, theta_1, x), color='red')
            plt.show()
       
    return theta_0, theta_1, cost_list    
    
# 입력 변수(집 크기) 초기화 (모든 집 평수 데이터를 1/10 크기로 줄임)
house_size = np.array([0.9, 1.4, 2, 2.1, 2.6, 3.3, 3.35, 3.9, 4.4, 4.7, 5.2, 5.75, 6.7, 6.9])

# 목표 변수(집 가격) 초기화 (모든 집 값 데이터를 1/10 크기로 줄임)
house_price = np.array([0.3, 0.75, 0.45, 1.1, 1.45, 0.9, 1.8, 0.9, 1.5, 2.2, 1.75, 2.3, 2.49, 2.6])

# theta 값들 초기화 (아무 값이나 시작함)
theta_0 = 2.5
theta_1 = 0

# 학습률 0.1로 200번 경사 하강
theta_0, theta_1, cost_list = gradient_descent(theta_0, theta_1, house_size, house_price, 200, 0.1)

# 결과 theta값
print(theta_0, theta_1)

# 경사 하강에 따른 손실 비용 그래프
print(plt.plot(cost_list))