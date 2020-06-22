import json

with open('data.json', 'r') as f:
    templates = json.load(f)

print(templates['customer'])
for line in templates['Objects']:
    print(line)

templates['customer'] = 'какой-то текст'

with open('data.json', 'w') as f:
    json.dump(templates, f)

with open('data.json', 'r') as f:
    templates = json.load(f)

print(templates['customer'])
