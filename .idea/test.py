import requests
import json

num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0
i =  1
# for i in range(10000):
#     url = "http://10.0.0.13:8083/game/gameShakeStart"
#     par = {
#         "jetton": "1"
#     }
#     h = {
#         "sessionId": "5b5ae83794da",
#         "Content-Type": "application/json"
#     }
#     r = requests.post(url, data=json.dumps(par), headers=h)
#     # print(type(r.json()))
#     # print(r.json()["data"]["odd"])
#     mm = r.json()["data"]["odd"]
#     # print(mm)
#     if mm == 24:
#         num1 += 1
#     if mm == 12:
#         num2 += 1
#     if mm == 8:
#         num3 += 1
#     if mm == 6:
#         num4 += 1
#     if mm == 4:
#         num5 += 1
#     if mm == 3:
#         num6 += 1
#     # print(mm)
# print(num1, num2, num3, num4, num5, num6)

for i in range(1000):
    url = "http://10.0.0.13:8083/game/gameNiuniuStart"
    par={
        "jetton":"100"
    }
    h = {
        "sessionId":"5b5ae83794da",
        "Content-Type": "application/json"
    }
    r = requests.post(url,data=json.dumps(par),headers=h)
    #print(type(r.json()))
    #print(r.json()["data"]["award"])
    mm = r.json()["data"]["award"]
    num1 = num1 + mm
print(num1)