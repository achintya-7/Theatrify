from appwrite.client import Client
from appwrite.services.database import Database

client = Client()

(client.set_endpoint('https://[]/v1')  # Your API Endpoint
 .set_project('')  # Your project ID
 .set_key('') # Your secret API key
 .set_self_signed()  
 )

database = Database(client)

result = database.list_documents('61eafd364852a5bccadb')
result2 = result['documents']
email_ids = []

for i in range(result['sum']):
    email_ids.append(result2[i]['emails'])

# gives all the email ids
print(email_ids)
