from google.cloud import storage
from google.oauth2 import service_account
import os
import uuid
import json
import random
import logging
from google.cloud import storage
import json
import firebase_admin
from firebase_admin import credentials, initialize_app,firestore


def clean_received_data(filename):
    # Open the JSON file for reading
    with open(filename, 'r') as file:
        data = file.read()

    # Remove newline characters
    data = data.replace('\n', '')

    # Parse the modified JSON data
    json_data = json.loads(data)

    # Do further processing with the JSON data

    # Optional: Save the modified JSON data to a new file
    with open('modified_data.json', 'w') as file:
        json.dump(json_data, file)

def upload_to_gcp_bucket(bucket_name, file_path, key_path, new_filename=None):
    """Uploads a file to a Google Cloud Storage bucket with an optional new filename."""
    # Instantiate a client using the service account key
    client = storage.Client.from_service_account_json(key_path)

    # Get the bucket
    bucket = client.get_bucket(bucket_name)

    # Extract the original filename from the file path
    original_filename = os.path.basename(file_path)

    # Determine the new filename
    if new_filename is None:
        new_filename = original_filename

    # Create a blob object and upload the file with the new filename
    blob = bucket.blob(new_filename)
    blob.upload_from_filename(file_path)

    print(f"File '{file_path}' uploaded to bucket '{bucket_name}' with new filename '{new_filename}' successfully!")



# Usage example

## logger config
# Create and configure logger
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
 
# Creating an object
logger = logging.getLogger()
 
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

##
# from pyloggers import CONSOLE


def get_id():
   id = uuid.uuid1()
   return str(id)



storage_cleint = storage.Client.from_service_account_json('compfox-367313-ad58ca97af3b.json')
def name_split(filename):
    # split the filename by underscore
    parts = filename.split('_')

    # extract the required substring
    name = parts[3][:-4]
    return name
import json

def send_bucket(json_data):
    bucket_name = 'checked_upload'
    blob_name = 'my-json-file.json'
    
    # Create a storage client
    storage_client = storage.Client.from_service_account_json('compfox-367313-ad58ca97af3b.json')
    
    # Get the bucket
    bucket = storage_client.bucket(bucket_name)
    
    # Create a new blob and upload the JSON data to it
    blob = bucket.blob(blob_name)
    blob.upload_from_string(json.dumps(json_data), content_type='application/json')

    print(f"JSON data uploaded to gs://{bucket_name}/{blob_name}")


async def get_first_100():
    bucket_name = "regular_final_html"
    filenames=[]
    count=0
    # Get a reference to the bucket
    bucket = storage_cleint.get_bucket(bucket_name)
    # List all HTML files in the bucket
    data={}
    dict_list={}
    pages=[]
    blobs = bucket.list_blobs(prefix="", delimiter="/")
    for blob in blobs:
        count+=1
        if count<=100:
            if blob.name.endswith('.pdf'):
                print(blob.name, "count:",count)
                name = name_split(blob.name)
                filenames.append(name)
                html_blob = bucket.blob(blob.name)
                html_contents = html_blob.download_as_string().decode("utf-8")
                logger.debug(" The html is as follows: {} --DONE".format(html_contents))
                # print(html_contents)
                # exit()
                id=get_id()
                data[id]={}
                data[id]['filename']=name
                data[id]['status']='warning'
                my_dict = json.loads(html_contents)
                data[id]['html']=my_dict
        else:
            break
    
    json_data = json.dumps(data)
    with open('db4_data.json', 'w') as f:
        f.write(json_data)
    return "done"



def get_json():
#client = storage.Client(Credentials=google_credentials)
    bucket_name = "regular_final_html"

    # Get a reference to the bucket
    bucket = storage_cleint.get_bucket(bucket_name)
    # List all HTML files in the bucket
    blobs = bucket.list_blobs(prefix="", delimiter="/")
    filenames = []
    dict_list = []
    keys = []
    data = {}
    for blob in blobs:
        if blob.name.endswith('.pdf'):
            name = name_split(blob.name)
            filenames.append(name)
            html_blob = bucket.blob(blob.name)
            html_contents = html_blob.download_as_string().decode("utf-8")
            my_dict = json.loads(html_contents)
            for key, value in my_dict.items():
                # print(key)
                keys.append(key)
                id = random.randint(0,10000)
                data[id] = {"text": value, "filename":name}
        if len(keys) >100:
            dict_list.append(data)
            data = {}
            keys = []
    # convert the list to JSON
    json_data = json.dumps(dict_list)

    # save the JSON data to a file
    with open('db4_data.json', 'w') as f:
        f.write(json_data)
    with open('list_of_left.txt','w') as p:
        p.write(filenames)

    
def load_db():
    if os.path.isfile("db4_data.json"):
        duck=open("db4_data.json","r")
        return duck.read()
    else:
        logger.error("Not found db in load_db function...")
        return "Not found db."
cred = credentials.Certificate(r"./qa-compfox-firebase-adminsdk-y690i-09111177d6.json")
initialize_app(cred) 
def get_work_id_user2(id):
    


    db = firestore.client()

    doc_ref = db.collection('html').document(id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        print(f"No such document with ID '{id}'")
        return None



def update_status(json_file, id, new_status):
    with open(json_file, 'r') as file:
        data = json.load(file)  # Load the JSON data

    if id in data:
        data[id]['status'] = new_status  # Update the status for the specified ID

    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

# print(get_work_id_user2("0de4f4f5-ecaf-11ed-acec-ec2e98e427c4"))