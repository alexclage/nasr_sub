from create_db import main as create_db
from data_retrieve.scraper import NASR_base
from datetime import datetime
import dotenv
dotenv.load_dotenv(override=True)
import importlib
import logging
import os
from tools.file_manager import file_deleter

logging.basicConfig(
    filename="C:/Users/alexm/Code/development/airplane/nav_data/logs/db_logs/db_manager.log",
    format='%(asctime)s %(levelname)-8s %(name)s \t %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

def Set_Meta(date: datetime.date, version_: str, table_name=""):
        
        Base = importlib.import_module(f"models.{version_}_models").Base
        
        if table_name != "":
            for table in Base.metadata.sorted_tables:
                if table_name == table.name:
                    table.info["last_update"] = date
                    logger.info(f"{table_name} Metadata updated with date {str(date)}")

        else:
            for table in Base.metadata.sorted_tables:
                table.info["last_update"] = date
                logger.info(f"{table.name} Metadata updated with date {str(date)}")

class DB_Compare:
    def __init__(self):
        self.nasr_base = NASR_base()

    def new_update(self, version_):

        Base = importlib.import_module(f"models.{version_}_models")
        Base = Base.Base

        # Compare the current data in the database with the current NASR data publish date
        # If database data is older than the NASR data, return True

        self.nasr_date = self.nasr_base.current_date

        return all([table.info["last_update"] < self.nasr_date for table in Base.metadata.sorted_tables])

class Version_Control:
    def __init__(self):
        self.current_db = os.getenv("CURRENT_DB")
        self.future_db = os.getenv("FUTURE_DB")

def update_db():

    # Order of operations is critical
    # Any errors will result in corrupt file names and data
    # files of concern are:
    #  - current_config.json/future_config.json
    #  - current_models.py/future_models.py    
    #  - zips directory:
    #       - current/(all files)
    #       - future/(all files)

    # Steps:
    # rename current_models.py to {current_csv_date}_models.py and place in models/archive/
    os.rename(os.getenv("CURRENT_MODELS_LOC"), os.getenv("ARCHIVE_MODELS_LOC")+os.getenv("CURRENT_DB_DATE")+"_models.py")
    logger.info(f"{os.getenv('CURRENT_DB_DATE')+'_models.py'} archived")

    # delete current_models.py
    file_deleter(os.getenv("CURRENT_MODELS_LOC"))
    logger.info(f"current_models.py deleted")

    # rename future_models.py to current_models.py
    os.rename(os.getenv("FUTURE_MODELS_LOC"), os.getenv("CURRENT_MODELS_LOC"))
    logger.info(f"future_models.py renamed to current_models.py")

    # rename current_config.json to {current_csv_date}_config.json and place in model_config/archive/
    os.rename(os.getenv("CURRENT_MODELS_CONFIG_LOC"), os.getenv("ARCHIVE_MODELS_CONFIG_LOC")+os.getenv("CURRENT_DB_DATE")+"_config.json")
    logger.info(f"current_config.json archived")

    # delete current_config.json
    file_deleter(os.getenv("CURRENT_MODELS_CONFIG_LOC"))

    # rename future_config.json to current_config.json
    os.rename(os.getenv("FUTURE_MODELS_CONFIG_LOC"), os.getenv("CURRENT_MODELS_CONFIG_LOC"))
    logger.info(f"future_config.json renamed to current_config.json")

    # delete current zips
    zip_loc = os.getenv("CURRENT_ZIP_LOC")
    for file in os.listdir(zip_loc):
        file_path = zip_loc.strip(zip_loc.split("/")[-1])
        file_deleter(file_path)
    logger.info(f"/zips/current deleted")

    # replace .env CURRENT_DB_DATE wiith FUTURE_DB_DATE
    dotenv_file = dotenv.find_dotenv()
    dotenv.set_key(dotenv_file, "CURRENT_DB_DATE", os.getenv("FUTURE_DB_DATE"))
    logger.info(f"CURRENT_DB_DATE updated to {os.getenv('FUTURE_DB_DATE')}")

    # replace .env CURRENT_DB_LOC wiith FUTURE_DB_LOC
    dotenv.set_key(dotenv_file, "CURRENT_DB_LOC", os.getenv("FUTURE_DB_LOC"))
    logger.info(f"CURRENT_DB_LOC updated to {os.getenv('FUTURE_DB_LOC')}")



if __name__ == "__main__":

    nasr_base = NASR_base()
    db_date = datetime.strftime(os.getenv("CURRENT_DB_DATE").capitalize(), "%b%y").date()

    if nasr_base.current_date <= db_date:
        update_db()
        create_db(version_ = "future")
        logger.info("Database Update Detected!")

    else:
        pass