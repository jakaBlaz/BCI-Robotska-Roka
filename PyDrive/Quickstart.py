from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file1 = drive.CreateFile({'id': '1bVhKqEmIx_YaTZDezwMvxTC3lO0A8zBV'})

# Fetches all basic metadata fields, including file size, last modified etc.
#file1.FetchMetadata()

# Fetches all metadata available.
file1.FetchMetadata(fields='modifiedDate')
print(file1)
"""
# Fetches the 'permissions' metadata field.
file1.FetchMetadata(fields='permissions')
# You can update a list of specific fields like this:
file1.FetchMetadata(fields='permissions,labels,mimeType') 
"""