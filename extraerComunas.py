
import json
from os import system

system('cls')

with open('regiones-comunas.json', 'r', encoding='utf-8') as file:
    regiones = json.load(file)
    
    
comunas = []

for region in regiones['regions']:
    for com in region['communes']:
        data={}
        fields={}
        data['model'] = 'acisApi.comuna'
        reg_id = region['number']
        fields['reg_id'] = reg_id
        fields['nom_com'] = com['name']
        data['fields'] = fields
        comunas.append(data)

with open('comunas.json', 'w', encoding='utf-8') as outfile:
    json.dump(comunas, outfile, ensure_ascii=False, indent=4)

  