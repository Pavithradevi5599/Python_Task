import re
import requests
from bs4 import BeautifulSoup
url="https://www.w3schools.com/python"
response=requests.get(url)
html_content=response.text
pattern="<.*?>(.*?)</.*?>"
matches=re.findall(pattern,html_content)
extracted_text='\n'.join(matches)
with open('Regex.txt','w')as file:
    file.write(extracted_text)
print("Text extracted and saved successfully")
