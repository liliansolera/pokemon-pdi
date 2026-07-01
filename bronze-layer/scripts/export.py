import json
import time
import requests
from pathlib import Path
import logging

file_dir = Path(__file__).resolve().parent   # local do script
bronze_root = file_dir.parent                # diretorio 'acima' do script, nesse caso bronze directory

pokemon_dir = bronze_root / "pokemon"
species_dir = bronze_root / "pokemon-species"
encounters_dir = bronze_root / "encounters"
evolution_dir = bronze_root / "evolution-chain"

logging.basicConfig(
    # LOGGING
    # usando logging para armazenar os dados de processamento em vez de apenas printar
    # precisa rodar 1 unica vez, então fica fora do loop

    level=logging.INFO, # nivel minimo (antes disso só tem debug, os demais sao mais criticos, esse é informativo)
    format="%(asctime)s [%(levelname)s] %(message)s", # formato do log (time, level, mensagem; ex.: timestamp, INFO, 'armazenado com sucesso')
        handlers=[
        logging.StreamHandler(),            # mostra na tela, em tempo real
        logging.FileHandler("export.log"),  # guarda no arquivo
    ],
)

def get_response(url):

    response = requests.get(url)
    response.raise_for_status()
    return response

def create_file(file_name,folder,data):
    with open(
            folder / f"{file_name}.json",
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                data, file, ensure_ascii=False, indent=4
            )  # ensure_ascii = false permite caracteres especiais


try:
    for i in range(1, 152): # como eu deixo isso dinamico? caso mude a quantidade de um dia pro outro

        url_species = f"https://pokeapi.co/api/v2/pokemon-species/{i}"
        response_species = get_response(url_species)
        species = response_species.json()
        file_name = f'{i}_{species["varieties"][0]["pokemon"]["name"]}'
        create_file(file_name, species_dir, species)

        logging.info(f'File {file_name} exported to SPECIES folder.')


        evolution_id = species["evolution_chain"]["url"].split("/")[-2]
        url_evolution = f"https://pokeapi.co/api/v2/evolution-chain/{evolution_id}"
        response_evolution = get_response(url_evolution)
        evolution = response_evolution.json()
        create_file(evolution_id, evolution_dir, evolution)

        logging.info(f'evolution_id {evolution_id} exported to EVOLUTION-CHAIN folder.')

        url_pokemon = f"https://pokeapi.co/api/v2/pokemon/{i}"
        response_pokemon = get_response(url_pokemon)
        pokemon = response_pokemon.json()
        create_file(file_name, pokemon_dir, pokemon)

        logging.info(f'File {file_name} exported to POKEMON folder.')

        url_encounters = f"https://pokeapi.co/api/v2/pokemon/{i}/encounters"
        response_encounters = get_response(url_encounters)
        encounters = response_encounters.json()
        create_file(file_name, encounters_dir, encounters)

        logging.info(f'File {file_name} exported to ENCOUNTERS folder.')

        time.sleep(2)
    logging.info('End of processing')

except Exception as error:
    logging.error(f'Failed API call for pokemon_id {i}: {error}')
    #esse erro raiser aqui tá péssimo, tá jogando coisa q nao é da API pra cá e confundindo
