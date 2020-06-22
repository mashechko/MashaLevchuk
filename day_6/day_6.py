import json
import os
import tempfile


def dict_data(a, b, c):
    keys = []
    keys.extend(a.keys())
    keys.extend(b.keys())
    keys.extend(c.keys())
    values = []
    values.extend(a.values())
    values.extend(b.values())
    values.extend(c.values())
    data = {}
    for i in range(0, len(keys)):
        data[keys[i]] = values[i]

    return data


data_1 = {'name': 'Sasha'}
data_2 = {'last_name': 'Viktorov'}
data_3 = {'sur_name': 'Ivanov'}

new_data = dict_data(data_1, data_2, data_3)

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

with open(storage_path, 'w') as f:
    json.dump(new_data, f)

with open(storage_path, 'r') as f:
    storage = json.load(f)

print(storage)
