from logging import info
import random
import requests
response = requests.get('https://api.apify.com/v2/key-value-stores/ZsOpZgeg7dFS1rgfM/records/LATEST?utm_source=j2team&utm_medium=url_shortener')
data = response.json()
# tpHCM = f'Detail: {data["detail"][0]["name"]} \nDeath: {data["detail"][1]["death"]} \nCases: {data["detail"][1]["cases"]} \nCases Today: {data["detail"][1]["casesToday"]}'

detail = data["detail"]

for i in range(80):
    li = data["detail"][i]["name"]
    print(f'{i}.{li}')


# i = 0

# for i in detail:
#     info = f'Detail: {data["detail"][i]["name"]} \nDeath: {data["detail"][i]["death"]} \nCases: {data["detail"][i]["cases"]} \nCases Today: {data["detail"][i]["casesToday"]}'
#     print(info)
#     if i == 70 :
#         break

# print(detail)