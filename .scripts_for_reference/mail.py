import os
import random
from newsapi import NewsApiClient
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from appwrite.client import Client
from appwrite.services.database import Database

key_news = os.environ['NEWS_API']
key_email = os.environ['EMAIL_API']

# COLLECTING OF EMAILS FROM THE DATABASE
client = Client()

(client.set_endpoint(os.environ['APPWRITE_ENDPOINT'])  # Your API Endpoint
 .set_project(os.environ['APPWRITE_FUNCTION_PROJECT_ID'])  # Your project ID
 .set_key(os.environ['APPWRITE_API_KEY'])  # Your secret API key
 .set_self_signed())

database = Database(client)

result = database.list_documents('61eafd364852a5bccadb')
result2 = result['documents']
email_ids = []

for i in range(result['sum']):
    email_ids.append(result2[i]['emails'])



# GETTING THE NEWS
newsapi = NewsApiClient(api_key=key_news)

data = newsapi.get_everything(
    q='theatre',
    language='en',
    sort_by='relevancy',
)

articles = data['articles']
results = data['totalResults']

num = random.randint(0, 16)

title = articles[num]["title"]
content = articles[num]["content"]
url_article = articles[num]["url"]
url_image = articles[num]["urlToImage"]

# HTML TEMPLATE TO DISPLAY THE NEWS IN THE EMAIL
html_template = f"""
<center>
    <p style="font-size: 48px;"> {title} <p>
</center> <br> 
<center> 
    <img src={url_image}> <br>
</center>

<p style="font-size: 24px;"> {content} </p> <br>

<center> <a href={url_article}> <button style="font-size: large;">Full Article</button> </a> </center>
"""

print(email_ids)

# SENDING OF EMAIL
for ids in email_ids:
    message = Mail(from_email='achintya.x7.1@gmail.com',
                   to_emails=ids,
                   subject='your daily theatre news',
                   html_content=html_template)

    try:
        sg = SendGridAPIClient(key_email)
        response = sg.send(message)
        print(f'email sent : {ids}')
    except Exception as e:
        print(e)