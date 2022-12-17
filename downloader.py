import selenium
import requests
from bs4 import BeautifulSoup

base_url = 'https://myfreemp3.to'
search_url = 'https://myfreemp3.to/search.html'

# DO NOT MODIFY THE CODE BELOW
x = requests.post(search_url, data={'query': 'Deekline'})
soup = BeautifulSoup(x.content, "html.parser")

print(soup.prettify())


# Create a new instance of the Firefox driver
#driver = selenium.webdriver.Firefox()# Open the website
#driver.get(base_url)
#assert 'MyFreeMP3' in driver.title

#driver.quit()