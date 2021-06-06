import requests
from bs4 import BeautifulSoup
import re
from url_extractor import urls


r = requests.get(urls[0])


soup = BeautifulSoup(r.content, 'html5lib')

# Starts from a question keyword
# Ends in a ?
# a tag's href can point to another page which has the answer
# classname contains accordian
# question 
child_soup = soup.find_all(['a', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'div'])

questions={}
for elem in soup(text=re.compile(r'\s*((?:how|How|Can|can|what|What|where|Where|describe|Describe|Who|who|When|when|Why|why|Should|should|is|Is|I|Do|do|Are|are|Will|will)[^.<>?]*?\s*\?)')):
    #print(elem)
    questions[elem.strip()] = "Some Answer"

print(questions)


    