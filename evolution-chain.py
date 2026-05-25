import json
import requests
import os
import time

arquivos = os.listdir('C:\\Users\\Remakker\\PDI-lilian\\bronze-layer\\pokemon-species')

ids = []

for i in arquivos:
    if i.endswith('.json'):
        with open(f"C:\\Users\\Remakker\\PDI-lilian\\bronze-layer\\pokemon-species\\{i}", "r", encoding="utf-8") as f:
            pokemon = json.load(f)
        evolution_url = pokemon['evolution_chain']['url']
        evolution_id = evolution_url.split('/')[-2]
        ids.append(evolution_id)

ids_unique = list(set(ids))

try:
    for i in ids_unique:
        response = requests.get(f"https://pokeapi.co/api/v2/evolution-chain/{i}")
        evolution_chain = response.json()

        with open(f"C:\\Users\\Remakker\\PDI-lilian\\bronze-layer\\evolution-chain\\{i}.json", "w", encoding="utf-8",) as f:
            json.dump(evolution_chain, f, ensure_ascii=False, indent=4)
        time.sleep(2)
        print(f"Success. ID {i}")
except requests.RequestException as error:
     print(error)

print('Concluído')
