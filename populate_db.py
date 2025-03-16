import csv
from data_retrieve.scraper import NASR_base
from db_connector import DBConnector
import dotenv 
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file, override=True)

import logging
import importlib

from manage_db import Set_Meta
import os
from sqlalchemy.orm import Session


logger = logging.getLogger(__name__)

logging.basicConfig(
    filename="C:/Users/alexm/Code/development/airplane/nav_data/logs/db_logs/data_input.log",
    format='%(asctime)s %(levelname)-8s %(name)s \t %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
    )



def create_rows(file_: str, version_: str) -> list:

    """
    Returns a list of the respective model objects from rows of data within
    the .csv file
    Committing the rows to the database should be added separately for logging and 
    separation of responsibilities
    """

    # dynamically import the models module
    models = importlib.import_module(f"models.{version_}_models")

    no_models = 0

    # returnable list that will house model objects for each
    # row in .csv

    model_list = []

    # Model name is filename stripped of '.csv'

    model_name = file_.strip(".csv")

    with open(os.environ[f'{version_.upper()}_ZIP_LOC'] + file_, mode='r', encoding='latin-1') as file:

        data = csv.DictReader(file)

        # loop through data rows in dict

        for row in data:

            # get model instance from model instance dictionary

            try:
                model = getattr(models, model_name)
                model = model()

            except Exception as f:
                logger.error(f"Model {model_name} not found in models.py file")
                logger.error(f)
                raise f


            # loop through column names from data and setattr the model with the values

            for column_name, value in row.items():

                # reformat column name as .csv is all caps
                column_name = column_name.lower().strip(" ").replace(' ', '_')

                # check that data is compliant of not_null before adding to list

                # Check if the column has a not_null constraint
                column = model.__table__.columns.get(column_name)
                if column is None:
                    logger.error(f"Column {column_name} not found in {model_name}")
                    raise ValueError(f"Column {column_name} not found in {model_name}")
                if not column.nullable and value in (None, '', ' '):
                    logger.error(f"Column {column_name} in {model_name} cannot be null\nValues passed: {row}")
                    raise ValueError(f"Column {column_name} in {model_name} cannot be null. Values passed are {row}")

                try:
                    # set attribute of model to value in .csv
                    setattr(model, column_name, value)
                    
                except Exception as e:
                    logger.error(f"Error setting attribute {column_name} to {value} in {model_name}")
                    logger.error(e)
                    raise e

                # append to return list
                model_list.append(model)
                no_models += 1

    logger.info(f"{no_models} models created from {file_}")
    return model_list

def main(version_):

    rows_created = 0 # number of rows created
    nasr = NASR_base()


    db = DBConnector(f"{version_.upper()}_DB_LOC")

    Base = importlib.import_module(f"models.{version_}_models").Base

    Base.metadata.create_all(db.engine)

    # Loop through files in models dir

    for file in os.listdir(os.environ[f'{version_}_ZIP_LOC']):

        # eliminate all files that aren't data filled .csv files

        if file.endswith(".csv") and "DATA_STRUCTURE" not in file:

            # data_rows stores a list of model instances that have
            # NOT been committed to their respective tables.

            data_rows: list = create_rows(file, version_)

            # create a session to commit the data rows to the database

            with Session(db.engine) as session:

                for row in data_rows:

                    try:

                        session.add(row)
                        rows_created += 1
                    
                    except Exception as e:
                        logger.error(f"Error adding {row} to session")
                        logger.error(e)
                        raise e

                try:    
                    session.commit()
                except Exception as e:
                    logger.error(f"Error committing {file.strip('.csv')} to database")
                    logger.error(e)
                    for row in session.new:
                        try:
                            session.commit()
                        except Exception as e:
                            logger.error(f"Error committing {row} to database")
                            logger.error(e)
                            raise e

            logger.info(f"{len(data_rows)} rows committed to {file.strip('.csv')} table")

            Set_Meta(nasr.current_date, version_, table_name=file.strip('.csv'))

    return rows_created