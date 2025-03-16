from .config_tool import Configurator
from dotenv import load_dotenv
load_dotenv(override=True)
import json
import os
import time

def get_config(version_):
    with open(os.getenv(f"{version_.upper()}_MODELS_CONFIG_LOC"), "r") as json_file:
        reader = json.load(json_file)

    return reader

def get_primary_key_dict(
        primary_key_loc= "C:/Users/alexm/Code/development/airplane/nav_data/nasr_sub/model_config/primary_key.json",
):
    # * Implement automated primary key detection
    # * Implement automated foreign key detection
    # * Implement automated relationship detection
    # * Implement automated data type detection
    # * Implement automated nullable detection

    with open(primary_key_loc, "r") as json_file:
        reader = json.load(json_file)

    return reader

def main(version_):

    start = time.perf_counter()
    models_written = 0
    config_data = get_config(version_)
    primary_key_dict = get_primary_key_dict()
    config = Configurator(version_)

    for filename, layout in config_data.items():

        for model_name, column_data in layout.items():

            primary_keys = primary_key_dict[model_name] #get the primary keys for the model -> list
            
            config.add_model(model_name, column_data, primary_keys)
            models_written += 1

        #config.write_file()
    config.write_file()

    config.logger.info(f"{models_written} models written in {(time.perf_counter() - start)*1000:.2f} milliseconds")
    return models_written