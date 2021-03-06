from pydrive2.auth import GoogleAuth #potrebna knjiđnica PyDrive2, ki se jo dobi z pip install pydrive2
from pydrive2.drive import GoogleDrive

gauth = GoogleAuth() #Potrebno je imeti na kompu ali client_secrets.json ali pa mycreds.txt, ki ne pridejo s knjižnco zraven
# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)

##FUNKCIJE
def delete_file(file_id):
  file1 = drive.CreateFile({'parents': [{'id': '1eeA-y9DjF4zOuH4z5wkOB5nSehRtGneV'}],'id': file_id})
  file1.Delete()

def create_file(name,content):
  file1 = drive.CreateFile({'title': name,'parents': [{'id': '1eeA-y9DjF4zOuH4z5wkOB5nSehRtGneV'}]})  # Create GoogleDriveFile instance with title 'Hello.txt'.
  file1.SetContentString(content,encoding="utf-8")
  file1.Upload()
  print("File was created under the id %s" %(file1['id']))
  return file1

def list_files():
  final_file_list = []
  file_list = drive.ListFile({'q' : "'1eeA-y9DjF4zOuH4z5wkOB5nSehRtGneV' in parents and trashed=false" }).GetList()
  for file1 in file_list:
    print('title: %s, id: %s' % (file1['title'], file1['id']))
    final_file_list.append('title: %s, id: %s' % (file1['title'], file1['id']))
  return final_file_list

def get_file_metadata(file_id):
  file1 = drive.CreateFile({'id': file_id})
  # Fetches all basic metadata fields, including file size, last modified etc.
  file1.FetchMetadata()
  print("File metadata: %s" %(file1))

#create_file("Testni_File.txt","Nek testni text, da vidim ce to dela kot more. abcčdefghijklmnoprsštuvzž")
#files = list_files()
#delete_file("16J9sx2qh2-fFsECfzFDWtk_E1iN6UnVY")


'''
# Fetches all metadata available.
file5.FetchMetadata(fields='modifiedDate')
print(file1)
#
# Fetches the 'permissions' metadata field.
file5.FetchMetadata(fields='permissions')
# You can update a list of specific fields like this:
file5.FetchMetadata(fields='permissions,labels,mimeType')'''