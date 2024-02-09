import re
html="<h1>Welcome to all</h1>"
html2="<p>Hello</p>"
html3="<h2>Good day</h2>"
html4="<h3>Good morning</h3>"
h=html+html2+html3+html4
pattern="<.*?>(.*?)</.*?>"
matches=re.findall(pattern,h)
extracted_text='\n'.join(matches)
with open('Regex.txt','w')as file:
    file.write(extracted_text)
print("Text extracted and saved successfully")