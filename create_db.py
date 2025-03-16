from data_retrieve.scraper import NASR_base
import dotenv
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file, override=True)
import json
import logging
from model_config.create_models import main as create_models
import os
import pandas as pd
import sys
from tools.zip_file_tools import NASR_Zip

logging.basicConfig(
    filename="C:/Users/alexm/Code/development/airplane/nav_data/nasr_sub/logs/main.log",
    format='%(asctime)s %(levelname)-8s %(name)s \t %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

def fix_csv(version_):

    with open(os.getenv("COL_NAME_FIX")) as json_file:

        col_name_fix = json.load(json_file)

        for file, col_names in col_name_fix.items():
            df = pd.read_csv(os.getenv(f"{version_.upper()}_ZIP_LOC")+file+".csv", encoding="Latin-1", low_memory=False)
            df.columns = col_names
            df.to_csv(os.getenv(f"{version_.upper()}_ZIP_LOC")+file+".csv", index=False)


    for file in os.listdir(os.getenv(f"{version_.upper()}_ZIP_LOC")):
        if file.endswith(".csv") and "DATA_STRUCTURE" not in file:
            df = pd.read_csv(os.getenv(f"{version_.upper()}_ZIP_LOC")+file, encoding="Latin-1", low_memory=False)
            df.drop_duplicates(inplace=True)
            df.to_csv(os.getenv(f"{version_.upper()}_ZIP_LOC")+file, index=False)
            
def get_zips(version_):
    # * Initialize the NASR base
    nasr_base = NASR_base()

    download_method = getattr(nasr_base, f"download_{version_}_zip")
    download_method = download_method(path=os.getenv(f"{version_.upper()}_ZIP_LOC"))
    logger.info(f"{version_.capitalize()} NASR Zip downloaded")

    fix_csv(version_)

    db_date = getattr(nasr_base, f"{version_}_date")
    db_path = os.getenv("DB_DIR")
    dotenv.set_key(dotenv_file, f"{version_.upper()}_DB_DATE", db_date.strftime("%b%y").upper())
    dotenv.set_key(dotenv_file, f"{version_.upper()}_DB_LOC", db_path+db_date.strftime("%b%y").upper()+".db")
    
def configure_models(version_):
    # * Initialize the NASR Zip
    nasr_zip = NASR_Zip(version_)

    nasr_zip.write_nasr_specs()

    logger.info(f"NASR Specs written to file")

def create_rows(version_):

    no_models_created = create_models(version_)

    logger.info(f"{no_models_created} models created")

    from populate_db import main as populate_db

    rows_created = populate_db(version_)

    logger.info(f"{rows_created} rows created")

    return rows_created

def create_database(version_):

    get_zips(version_)
    sys.stdout.write("Zips downloaded\r")

    configure_models(version_)
    sys.stdout.write("Models configured\r")

    rows_created = create_rows(version_)
    sys.stdout.write("Rows created\r")

    print(f"{version_} Database Populated with {rows_created} rows")

def main(version_ = ""):

    if version_ == "":
        
        for version in ["current","future"]:

            create_database(version)

    else:
        create_database(version_)            

if __name__ == "__main__":
        
    for version_ in ["current","future"]:

        get_zips(version_)
        sys.stdout.write("Zips downloaded\r")

        configure_models(version_)
        sys.stdout.write("Models configured\r")

        rows_created = create_rows(version_)
        sys.stdout.write("Rows created\r")

        print(f"{version_} Database Populated with {rows_created} rows")

