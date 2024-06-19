import urllib3
from bs4 import BeautifulSoup
from requests import request
import lxml
from tqdm import tqdm

year=input("Enter the year: ")

url = "http://www.imdb.com/search/title?release_date=" + year + ',' + year + '&title_type=feature'
ourUrl = urllib3.PoolManager().request('GET', url).data
soup = BeautifulSoup(ourUrl, "lxml")
i = 1
movieList = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})
for div_item in tqdm(movieList):
    div = div_item.find('div',attrs={'class':'lister-item-content'})
    print (str(i) + '.')
    header = div.findChildren('h3',attrs={'class':'lister-item-header'})
    print ('Movie: ' + str((header[0].findChildren('a'))[0].contents[0].encode('utf-8').decode('ascii', 'ignore')))
    i += 1