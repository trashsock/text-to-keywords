# pip install requests

import requests
from pdfRead import ExtractTextFromPDF
from docRead import ExtractTextFromDocx
import time
from pathlib import Path
import json

# ===================================================================================

# Check in the uploads folder and call the respective function according to extension

def performStep1():

    file_data = ""

    for child in Path('uploads').iterdir():
        if child.is_file():
            filename = child.name
            # We're expecting only 1 file in the folder

    extension = filename.rsplit('.', 1)[1].lower()
    print("File Extension Is: ", extension)

    if extension=="pdf":
        file_data = ExtractTextFromPDF("uploads/"+filename)
    elif extension=="docx":
        file_data = ExtractTextFromDocx("uploads/"+filename)
    else:
        print("Invalid File Type !")

    send_step1_APIRequest(file_data) # Perform the API request by passing the File Text

# ===================================================================================

# Define Step 1 API Request Function

def send_step1_APIRequest(file_data):
    headers = {
            'action': 'save_imported_item',
            'title': 'sample',
            'text': file_data,
            'country': 'fi',
            'token': 'demo',
            'item':'sample_data'
            }

    url = "https://megatron.headai.com/Utils"
    resp = requests.post(url, headers=headers)
    # print("===================== STEP 1 =====================")
    print("Upload Status Code : " + str(resp.status_code))

    if resp.status_code == 200:
        print("Success")
        data = json.loads(resp.text)
        print(data)
    else:
        print("Failure")

# ===================================================================================

# STEP 2(a)
def send_2a_APIRequest():
    headers = {
            'action': 'build_imported_data_analysis',
            'title': 'sample',
            'output': 'json',
            'country': 'fi',
            'language':'en',
            'token': 'demo',
            'item':'sample_data',
            'update':'false'
        }

    url = "https://megatron.headai.com/Utils"
    resp = requests.post(url, headers=headers)
    # print("===================== STEP 2A =====================")
    print("Analysis Status Code : " + str(resp.status_code))

    if resp.status_code == 200:
        print("Success")
        data = json.loads(resp.text)
        print(data)
        # print("===================== JSON URL =====================")
        print("JSON URL => ", data["location"])
    else:
        print("Failure")

# ===================================================================================

# Step 2(b)
def send_2b_APIRequest():
    headers = {
            'action': 'check_imported_items_building_status',
            'country': 'fi',
            'token': 'demo',
            'item':'sample_data',
        }
    
    url = "https://megatron.headai.com/Utils"
    resp = requests.post(url, headers=headers)
    # print("===================== STEP 2B =====================")
    print("Build Status Code : " + str(resp.status_code))

    if resp.status_code == 200:
        print("Success")
        data = json.loads(resp.text)
        print(data)
    else:
        print("Failure")

# ===================================================================================

# Step 3
def step3MindMapAPIRequest():
    headers = {
            'language': 'en',
            'country': 'fi',
            'months': '12',
            'size':'10000',
            'ontology':'headai',
            'output':'json',
            'update':'true',
            'noise':'full',
            'token':'demo',
            'dataset':'imported_data',
            'item':'sample_data',
        }
    
    url = "https://megatron.headai.com/TextToMindMap"
    resp = requests.post(url, headers=headers)
    # print("===================== STEP 3 - MindMap =====================")
    print("Mind-Map Status Code : " + str(resp.status_code))

    if resp.status_code == 200:
        print("Success")
        data = json.loads(resp.text)
        print(data)
    else:
        print("Failure")

# ===================================================================================
def checkItemsAddedAPIRequest():
    headers = {
            'action': 'check_token_items',
            'token':'demo',
        }
    
    url = "https://megatron.headai.com/Utils"
    resp = requests.post(url, headers=headers)
    # print("===================== Check Items Added for Token - demo =====================")
    print("Check Items Status Code : " + str(resp.status_code))

    if resp.status_code == 200:
        print("Success")
        data = json.loads(resp.text)
        print(data)
    else:
        print("Failure")

# ===================================================================================


# Call all the methods defined in sequence

performStep1()
# send_step1_APIRequest() will be called internally by performStep1()
send_2a_APIRequest()
send_2b_APIRequest()
checkItemsAddedAPIRequest()
step3MindMapAPIRequest()
