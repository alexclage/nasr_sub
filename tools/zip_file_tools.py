import csv
from dotenv import load_dotenv
load_dotenv()
import json
import logging
import os
import time

class NASR_Zip:
    def __init__(self, version_):

        self.logger = logging.getLogger(__name__)

        logging.basicConfig(
            filename="C:/Users/alexm/Code/development/airplane/nav_data/logs/zip_file_logs/table_config.log",
            format='%(asctime)s %(levelname)-8s %(name)s \t %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S'
            )


        self.zip_loc = os.environ[f"{version_.upper()}_ZIP_LOC"]
        self.json_config = os.environ[f"{version_.upper()}_MODELS_CONFIG_LOC"]

        self.cats = []
        self.file_dict = {}
        self.file_spec_dict = {}
        self.structure_kward = "DATA_STRUCTURE"

    def get_file_cat(self,first_letters):

        self.file_dict[first_letters] = {
            "layout":[],
            "data":[]
        }

        for file in os.listdir(self.zip_loc):
            if file.startswith(first_letters):
                if "DATA_STRUCTURE" in file:
                    self.file_dict[first_letters]["layout"].append(file)

                elif file.endswith(".csv"):
                    self.file_dict[first_letters]["data"].append(file)

    def get_cat_file_specs(self,first_letters):

        # Creates a dict of specifications for each file in the NASR data
        """
        {
        "APT": {
            "APT_ARS": [
                {
                    "Column Name": "EFF_DATE",
                    "Max Length": "10",
                    "Data Type": "VARCHAR",
                    "Nullable": "No"
                },
                ...
            }
        }
        """

        if first_letters not in self.file_dict.keys():
        #if not hasattr(self, "file_dict"):
            self.get_file_cat(first_letters)

        if first_letters not in self.file_spec_dict.keys():
            self.file_spec_dict[first_letters] = {}

        try:
            layout_file = self.file_dict[first_letters]['layout'][0]
        except IndexError as e:
            self.logger.critical(f'{first_letters} not in file_dict: {print(self.file_dict[first_letters])}')
            raise e
        
        with open(self.zip_loc+"/"+layout_file, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            header = next(reader)
            for row in reader:
                if row[0] not in self.file_spec_dict[first_letters].keys():
                    self.file_spec_dict[first_letters][row[0]] = [
                        {
                            header[1]:row[1].strip(" "),
                            header[2]:row[2],
                            header[3]:row[3],
                            header[4]:row[4]
                        },
                    ]

                elif row[0] in self.file_spec_dict[first_letters].keys():

                    self.file_spec_dict[first_letters][row[0]].append(
                        {
                            header[1]:row[1].strip(" "),
                            header[2]:row[2],
                            header[3]:row[3],
                            header[4]:row[4]
                        },
                    )

    def get_nasr_cats(self):

        ## Creates a list held in self.cats of all the categories (File Name) in the NASR data

        file_names = os.listdir(self.zip_loc)
        for file in file_names:
            if file.endswith(".csv"):
                cat_listed = file.split("_")
                if len(cat_listed) == 1:
                    cat = cat_listed[0].strip(".csv")
                else:
                    cat = cat_listed[0]
                if cat not in self.cats:
                    self.cats.append(cat)
       
    def write_nasr_specs(self):

        if len(self.cats) == 0:
            self.get_nasr_cats()

        for cat in self.cats:

            self.get_cat_file_specs(cat)

        with open(self.json_config, "w") as json_file:
            json_ = json.dumps(self.file_spec_dict, indent=4)
            json_file.write(json_)
            self.logger.info(f'{len(self.file_spec_dict)} items written to {self.json_config}')


        

if __name__ == "__main__":

    start = time.perf_counter()
    NASR = NASR_Zip()
    NASR.write_nasr_specs()
    NASR.logger.info(f"Table update complete")
    NASR.logger.info(f"Run time: {(time.perf_counter() - start)*1000:.2f} milliseconds")