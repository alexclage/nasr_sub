import os
import json
import PyPDF2

def extract_unique_keys_from_pdf(pdf_path):
    unique_keys = []
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text = page.extract_text()
            # Assuming unique keys are identifiable in the text
            # Add your logic here to extract unique keys from the text
            # For example, if unique keys are prefixed with "Key: "
            for line in text.split('\n'):
                if "ordered by" in line:
                    try:
                        keys_ = line.split("ordered by")[1].strip().lower()
                        unique_keys.append(keys_.split(", "))
                    except IndexError:
                        print(line)
                        continue
    return unique_keys

def update_primary_key_json(json_path, unique_keys):
    # with open(json_path, 'r') as json_file:
    #     try:
    #         data = json.load(json_file)
    #     except json.JSONDecodeError:
    #         print()
    
    # for model, keys in unique_keys.items():
    #     if model in data:
    #         data[model].extend(keys)
    #     else:
    #         data[model] = keys
    
    with open(json_path, 'w') as json_file:
        #json.dump(data, json_file, indent=4)
        json.dump(unique_keys, json_file, indent=4)


if __name__ == "__main__":
    zip_folder = "C:/Users/alexm/Code/development/airplane/nav_data/zips"
    json_path = "C:/Users/alexm/Code/development/airplane/nav_data/model_config/primary_key_from_pdf.json"
    
    unique_keys = {}
    
    for file_name in os.listdir(zip_folder):
        if file_name.endswith(".pdf"):
            pdf_path = os.path.join(zip_folder, file_name)
            model_name = file_name.split('.')[0]  # Assuming model name is the file name without extension
            keys = extract_unique_keys_from_pdf(pdf_path)
            unique_keys[model_name] = keys
    
    update_primary_key_json(json_path, unique_keys)
