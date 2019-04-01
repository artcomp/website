#encoding=utf-8
import json
import scrap
from requests import get

def main():

	x = get('http://api.geonames.org/searchJSON?formatted=true&q=london&maxRows=3&lang=es&username=artdcomp&style=short')
	print x.text
	# y = json.loads(x)

	# for each in i['geonames']:
	# 	print each['name']



if __name__ == '__main__':
	main()