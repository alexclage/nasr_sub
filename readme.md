# NASR Subscription to Database

## Getting NASR zip file and generating config files

Ensure all file locations are set properly in nav_data.env file before proceeding

### Step 1

 > File - nav_data/data_retrieve/scraper.py
 > Create an instance of NASR_base
 > NASR_base has to methods; .download_current_zip() or .download_future_zip()
 > This will retrieve the respective zip file and place them in the "zips" directory

### Step 2

 > File - nav_data/tools/zip_file_tools.py
 > Create an instance of NASR_Zip
 > NASR_Zip has a master method that will generate the necessary config files for each of the files in the zips directory
 > Run NASR_Zip method .write_nasr_specs() to generate these config files

## Create models in models.py

This step creates a file named models.py which houses schema for all models within the NASR csv files
The models.py file is generated dynamically in order to account for changes in filenames or model names
Most errors should be collected and printed within the logs/zip_file_logs/table_config.log file

 > File - nav_data/model_config/create_models.py
 > Running the file as a script or importing the main() function will accomplish the same thing
 > All models will be generated with the schema provided in model_config directory .json files

