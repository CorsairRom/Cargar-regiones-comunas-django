import json
from os import system

system('cls')

with open('countries.json', 'r', encoding='utf-8') as file:
    countries = json.load(file)
    
    
countryDjango = []

for country in countries['countries']:
    data = {}
    fields = {}
    data['model'] = 'acisApi.paises'
    nombre = country['name_es']
    codigo = country['code_2']
    fields['name'] = nombre
    fields['code'] = codigo
    data['fields'] = fields
    countryDjango.append(data)

with open('countries-Django.json', 'w', encoding='utf-8') as outfile:
    json.dump(countryDjango, outfile, ensure_ascii=False, indent=4)
