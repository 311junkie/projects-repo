import json
import os
print(os.listdir())
print(os.getcwd())
print(os.chdir("./remodel"))
print(os.getcwd())
with open('data.json') as f:
    data = json.load(f)


#print(data['kitchen']['width'])
#print(data.get('kitchen'))


counter = 0
sqft_total = 0
for room in data:
    #length & width values provided in inches
    data[room]['sqft'] = int(data[room]['length'])/12 * int(data[room]['width'])/12
    print(room + ' : ' + str(data[room]['sqft']))
    sqft_total += data[room]['sqft']

print(f'Total sqft : {sqft_total:.2f}')