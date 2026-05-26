import json
import time

import requests

try:
    for i in range(1, 152):
        response_pokemon = requests.get(
            f"https://pokeapi.co/api/v2/pokemon-species/{i}"
        )
        response_encounters = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{i}/encounters"
        )

        pokemon = response_pokemon.json()
        encounters = response_encounters.json()

        pokemon_name = pokemon["varieties"][0]["pokemon"]["name"]
        with open(
            f"C:\\Users\\Remakker\\PDI-lilian\\pokemon-pdi\\bronze-layer\\pokemon-species\\{i}_{pokemon_name}.json",
            "w",
            encoding="utf-8",
        ) as arquivo_pokemon:
            json.dump(
                pokemon, arquivo_pokemon, ensure_ascii=False, indent=4
            )  # ensure_ascii = false permite caracteres especiais

        with open(
            f"C:\\Users\\Remakker\\PDI-lilian\\pokemon-pdi\\bronze-layer\\encounters\\{i}_{pokemon_name}.json",
            "w",
            encoding="utf-8",
        ) as arquivo_encounter:
            json.dump(encounters, arquivo_encounter, ensure_ascii=False, indent=4)
        print(f"ID {i} armazenado com sucesso")
        time.sleep(2)
    print("Processamento concluído")
except requests.RequestException as error:
    print(error)
