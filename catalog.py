import json
try:
    with open('Text_8.json') as a:
        catalog = json.loads(a.read())
except (FileNotFoundError, json.decoder.JSONDecodeError):
    catalog = {}
for i in range(3):
    N = input("введите наименование товара: ")
    C = int(input('Введите количество товара'))
    if N in catalog:
        catalog[N] += C
    else:
        catalog[N] = C
with open('Text_8.json', 'w') as q:
    s = json.dumps(catalog)
    q.write(s)