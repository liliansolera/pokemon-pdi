import json
import time

import requests

try:
    for i in range(1, 152):
        # CHAMA ENDPOINTS
        response_pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}")
        response_pokemon_species = requests.get(
            f"https://pokeapi.co/api/v2/pokemon-species/{i}"
        )
        response_encounters = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{i}/encounters"
        )

        # ARMAZENA EM JSON
        pokemon = response_pokemon.json()
        pokemon_species = response_pokemon_species.json()
        encounters = response_encounters.json()

        pokemon_name = pokemon_species["varieties"][0]["pokemon"]["name"]

        # CRIA ARQUIVOS
        with open(
            f"C:\\Users\\Remakker\\PDI-lilian\\pokemon-pdi\\bronze-layer\\pokemon-species\\{i}_{pokemon_name}.json",
            "w",
            encoding="utf-8",
        ) as arquivo_pokemon:
            json.dump(
                pokemon_species, arquivo_pokemon, ensure_ascii=False, indent=4
            )  # ensure_ascii = false permite caracteres especiais

        with open(
            f"C:\\Users\\Remakker\\PDI-lilian\\pokemon-pdi\\bronze-layer\\encounters\\{i}_{pokemon_name}.json",
            "w",
            encoding="utf-8",
        ) as arquivo_encounter:
            json.dump(encounters, arquivo_encounter, ensure_ascii=False, indent=4)

        with open(
            f"C:\\Users\\Remakker\\PDI-lilian\\pokemon-pdi\\bronze-layer\\pokemon\\{i}_{pokemon_name}.json",
            "w",
            encoding="utf-8",
        ) as arquivo_poke:
            json.dump(pokemon, arquivo_poke, ensure_ascii=False, indent=4)

        print(f"ID {i} armazenado com sucesso")
        time.sleep(2)
    print("Processamento concluído")
except requests.RequestException as error:
    print(error)
