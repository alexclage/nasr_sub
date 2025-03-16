import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

import os

class DBConnector:

    def __init__(self, db_name: str):

        from dotenv import load_dotenv
        load_dotenv(override=True)

        self.logger = logging.getLogger(__name__)
        self.engine = create_engine(f"sqlite+pysqlite:///{os.getenv(db_name)}", pool_pre_ping=True)
        self.logger.info(f"Database connection established at {os.getenv(db_name)}")