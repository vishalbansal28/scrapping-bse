import pandas as pd
from pymongo import MongoClient
import os

# Connect to MongoDB
client = MongoClient('mongodb+srv://bvansalvb:G1eVPWbygD8a29Dq@cluster10.saldbsb.mongodb.net/?retryWrites=true&w=majority')
db = client['bse_data']
collection = db['extracted_data']

def upload_excel_data_to_mongodb(file_path):
    try:
        # Read data from the Excel file
        df = pd.read_excel(file_path)

        # Convert DataFrame to list of dictionaries
        data = df.to_dict(orient='records')

        # Insert data into MongoDB collection
        collection.insert_many(data)

        print("Data uploaded to MongoDB")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Get the directory of the current script and construct the file path to the Excel file
current_directory = os.path.dirname(__file__)
excel_file_path = os.path.join(current_directory, "extracted_data.xlsx")

# Call the function to upload data from the Excel file to MongoDB
upload_excel_data_to_mongodb(excel_file_path)
