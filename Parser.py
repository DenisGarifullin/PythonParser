import requests
from bs4 import BeautifulSoup

URL = 'http://www.66.rospotrebnadzor.ru/'
HEADERS = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}


def get_html(url, params=None):
	r = requests.get(url, headers=HEADERS, params=params)
	return r


def get_content(html):
	soup = BeautifulSoup(html, 'html.parser')
	items = soup.find_all('div', class_= 'asset-abstract')
	news = []
	for item in items:
		news.append({
		'title': item.find('h3',class_='asset-title').get_text(strip=True),
		'link': item.find('h3',class_='asset-title').find_next('a').get('href'),
		'date': item.find('div', class_='asset-metadata').find_next('span',class_='metadata-entry metadata-publish-date').get_text(strip=True).replace('\n\t\t\t\t\n\t\t\t\n\t\t','')
		})
	print (news)
	print (len(news))
	return news
	
	
def parse():
	html = get_html(URL)
	if html.status_code == 200:
		news = get_content(html.text)
	else:
		print ('<Error>')


parse()