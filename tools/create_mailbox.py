import requests
from bs4 import BeautifulSoup

def generate(name=None, domain=None):
    if domain == None:
        url = 'https://email-fake.com/'
        req = requests.get(url)
        soup = BeautifulSoup(req.content, "html.parser")
        mail = soup.find_all("span", {"id": "email_ch_text"})[0].contents[0]
    else:
         # TODO Implement own trash-domains
        mail = f"DefaultOrRandom@{domain}"
    
    if name == None:
        return mail
    else:
        return f"{name}@{mail.split('@')[1]}"