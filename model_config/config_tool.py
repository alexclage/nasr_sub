from dotenv import load_dotenv
load_dotenv()
import json
import logging
import os
import textwrap


class model_base:

    def __init__(self):

        self.file_text = """
        from typing import List, Optional
        from sqlalchemy import ForeignKey, Integer, String
        from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

        """

        self.file_text += """
        class Base(DeclarativeBase):
        \tpass
        \n
        """
        self.file_text = textwrap.dedent(self.file_text)


class Configurator(model_base):

    def __init__(self, version_):
        
        super().__init__()

        self.version = version_

        self.logger = logging.getLogger(__name__)

        logging.basicConfig(
            filename="C:/Users/alexm/Code/development/airplane/nav_data/logs/zip_file_logs/table_config.log",
            format='%(asctime)s %(levelname)-8s %(name)s \t %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'
            )
        with open(os.getenv(f"CONFIG_FIX_LOC")) as json_file:
            self.config_corrections_dict = json.load(json_file)
        
    def add_model(self, model, column_data, primary_keys):

        """
        model: str - i.e. APT_BASE
        column_data: list - i.e. [{"Column Name": "APT_ID", "Data Type": "NUMBER", "Nullable": "No", "Max Length": 0},]
        primary_keys: list - i.e. ["APT_ID"]
        """

        ## Update config_dict with items found in config_corrections.json

        if model in self.config_corrections_dict.keys():
            for col in column_data:
                col_name = col["Column Name"].lower()
                if col_name in self.config_corrections_dict[model].keys():
                    col_data_dict = col
                    for attr_name, attr_value in self.config_corrections_dict[model][col_name].items():
                        col_data_dict[attr_name] = attr_value

                    column_data.pop(column_data.index(col))
                    column_data.append(col_data_dict)

        self.file_text += f"class {model}(Base):\n\n"
        self.file_text += f"\t__tablename__ = '{model.lower()}'\n"

        self.file_text += "\t__mapper_args__ = {"
        self.file_text += f"'primary_key': {primary_keys}" + "}\n\n\n"

        for column in column_data:

            column_name = column['Column Name'].lower().replace(' ', '_')

            self.file_text += f"\t{column_name}:"

            if column["Data Type"] == "VARCHAR":
                self.file_text += f" Mapped[str] = mapped_column(String({column['Max Length']})"

            elif column["Data Type"] == "NUMBER":
                self.file_text += f" Mapped[int] = mapped_column(Integer"

            if column["Nullable"] == "Yes":
                self.file_text += f", nullable=True"

            if column_name in primary_keys:
                self.file_text += f", primary_key=True)\n"
            else:
                self.file_text += f")\n"


        self.file_text += "\n"

    def dedent_text(self, text_):

        return textwrap.dedent(text_)

    def write_file(self):

        with open(os.getenv(f"{self.version}_MODELS_LOC"), "w") as model_file:

            dedented_text = self.dedent_text(self.file_text)

            model_file.write(dedented_text)