import urllib3
from bs4 import BeautifulSoup
from requests import request
import lxml
from tqdm import tqdm

year=input("Enter the year: ")

url = "http://www.imdb.com/search/title?release_date=" + year + ',' + year + '&title_type=feature'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
ourUrl = urllib3.PoolManager().request('GET', url,headers=headers).data
soup = BeautifulSoup(ourUrl, "lxml")


movieList = soup.findAll('div', attrs={'class': 'sc-b189961a-0 hBZnfJ'})
print(len(movieList))
for div_item in tqdm(movieList):
    div = div_item.find('div',attrs={'class':'ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN dli-title'})
    header = div.findChildren('a',attrs={'class':'ipc-title-link-wrapper'})
    print ('Movie: ' + str((header[0].findChildren('h3'))[0].contents[0].encode('utf-8').decode('ascii', 'ignore')))
    