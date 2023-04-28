import json

# person = {
#     'name': 'Luis Henrique',
#     'last_name': 'Beck',
#     'address': [
#         {'street': 'r1', 'number': 125},
#         {'street': 'r1', 'number': 125}
#     ],
#     "height": 1.80,
#     'dev': True
# }

# with open('teste.json', 'w', encoding='utf8') as archive: 
#     json.dump(person,
#             archive, 
#             ensure_ascii=False,
#             indent=2,
#             )

with open('teste.json', 'r', encoding='utf8') as archive:
    person = json.load(archive)
    print(person)
