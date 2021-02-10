# import requests
# import json
# url = "https://reqres.in/api/users?page=2"
#
# response=requests.get(url)
# print(response.status_code)
# print(response.content)
# json_data=response.content
#
# var= 0
#
# def validateJSON(jsonData):
#     try:
#         json.loads(jsonData)
#     except ValueError as err:
#         return False
#     return True
#
# isValid = validateJSON(json_data)
# print("Given JSON string is Valid", isValid)
# data = json.loads(json_data)
# for i in list(data.keys()):
#     print('value of parent node-->',i,'-is-->',data[i])
# for k in data.keys():
#     if isinstance(data[k],str) or isinstance(data[k],int):
#         print('0 child')
#     elif isinstance(data[k],dict):
#         for i in data.keys():
#             print(data[i])
#     else:
#         print('Length of the parent node is ',len(data[k]))
#         for child in data[k]:
#             for childk in child.keys():
#                 print(child[childk])
#

import pandas as pd

data_val=pd.read_csv('match.csv')
print(data_val)