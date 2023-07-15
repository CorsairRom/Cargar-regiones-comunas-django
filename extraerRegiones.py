
import json
from os import system

system('cls')

with open('regiones-comunas.json', 'r', encoding='utf-8') as file:
    regiones = json.load(file)

regions = []
    
for i,region in enumerate(regiones['regions']):
    data = {}
    fields = {}
    data['model'] = 'acisApi.region'
    id = region['number']
    orden = i+1
    nom_reg = region['namec']
    fields['id'] = id
    fields['orden'] = orden
    fields['nom_reg'] = nom_reg
    data['fields'] = fields
    regions.append(data)

with open('regiones.json', 'w', encoding='utf-8') as outfile:
    json.dump(regions, outfile, ensure_ascii=False, indent=4)