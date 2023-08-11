import json

with open('./lap.json') as json_file:
    data = json.load(json_file)

for lp  in data['laptop']:
   print(lp)
   print("Its running properly")