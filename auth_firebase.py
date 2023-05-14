# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import storage

# # Initialize Firebase app with credentials
# cred = credentials.Certificate('./qualitycheck-compfox-firebase-adminsdk-mbbbr-2eda7a2dd8.json')
# firebase_admin.initialize_app(cred, {
#     'storageBucket': 'qualitycheck-compfox.appspot.com'
# })

# # Get a reference to the storage service
# bucket = storage.bucket()


# # Download a file from Firebase Storage
# blob = bucket.blob('./billa.json')
# print(blob)
# blob.download_to_filename('billa_downloaded.json')

from firebase_admin import credentials, initialize_app, storage
def download_data_init():
    cred = credentials.Certificate(r"./qualitycheck-compfox-firebase-adminsdk-mbbbr-2eda7a2dd8.json")
    initialize_app(cred, {'storageBucket': 'qualitycheck-compfox.appspot.com'})

    bucket_name = 'qualitycheck-compfox.appspot.com'
    bucket = storage.bucket(bucket_name)

    source_blob_names = ['db4_data.json', 'db4_data_2k.json', 'db4_data_3k.json', 'db4_data_4k.json']#, 'file3.json', 'file4.json']
    destination_file_names = ['data1.json', 'data2.json','data3.json','data4.json']#, 'file3-downloaded.json', 'file4-downloaded.json']

    # bucket_name = 'qualitycheck-compfox.appspot.com'

    for i in range(len(source_blob_names)):
        blob = bucket.blob(source_blob_names[i])
        blob.download_to_filename(destination_file_names[i])
    
    return "Data Downloaded... Ready to go :)"

