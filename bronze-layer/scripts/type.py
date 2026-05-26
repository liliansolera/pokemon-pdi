import json
import os
import time

import requests

arquivos_pokemon = os.listdir(
    "C:\\Users\\Remakker\\PDI-lilian\\pokemon-pdi\\bronze-layer\\pokemon"
)

type_ids = []
for i in arquivos_pokemon:
    if i.endswith(".json"):
        with open(
            f"C:\\Users\\Remakker\\PDI-lilian\\pokemon-pdi\\bronze-layer\\pokemon\\{i}",
            "r",
            encoding="utf-8",
        ) as f:
            pokemon = json.load(f)
        for t in pokemon["types"]:
            type_url = t["type"]["url"]
            type_id = type_url.split("/")[-2]
            type_ids.append(type_id)


ids_unique = list(set(type_ids))

try:
    for i in ids_unique:
        response = requests.get(f"https://pokeapi.co/api/v2/type/{i}")
        type = response.json()

        with open(
            f"C:\\Users\\Remakker\\PDI-lilian\\pokemon-pdi\\bronze-layer\\type\\{i}.json",
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(type, f, ensure_ascii=False, indent=4)
        time.sleep(2)
        print(f"Success. Type ID {i}")
except requests.RequestException as error:
    print(error)

print("Concluído")
