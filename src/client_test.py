

from models.client import ClientModel
import json
import os

client_list = []
client = ClientModel('45578A', 'Lassina', 'OUATTARA', 'olassina@gmail.com', '45789fx', '79319964', 'bp59', 'Bobo')
client_list.append(client)
print(os.path._getfullpathname('students.json'))
for c in client_list:
    with open(os.path.join(os.path._getfullpathname('students.json')), 'w') as f:
        json.dump(client_list, f)
