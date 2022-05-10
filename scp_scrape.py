
import urllib.request
from bs4 import BeautifulSoup
from multiprocessing import Pool
import sys
import os

rng = range(2,10001)
all_valid = [0]
class_list = ['safe', 'euclid', 'keter', 'thaumiel', 'neutralized', 'apollyon', 'archon', 'explained', 'pending', 'esoteric-class', 'decomissioned']



print('Secure. Contain. Protect.')
#https://scp-wiki.wikidot.com/secure-facilities-locations

def getText(i):
	#
	cls = False
	url = urllib.request.urlopen("http://www.scp-wiki.net/scp-{:03d}".format(i))
	b = url.read()
	st = b.decode("UTF-8")
	soup = BeautifulSoup(st, 'lxml')
	pageCont = soup.find('div', id="page-content")
	if soup.find('div', id='u-adult-header') != None:
		url = urllib.request.urlopen("https://scp-wiki.wikidot.com/adult:scp-{:03d}/noredirect/true".format(i))
		b = url.read()
		st = b.decode("UTF-8")
		soup = BeautifulSoup(st, 'lxml')
		pageCont = soup.find('div', id="page-content")
	
		
	divs = pageCont.find_all('div')
	for d in divs:
		d.extract()
	para = pageCont.find_all('p')
	strng = ""
	#obj_atr = soup.select('div.obj')#soup.find('div', class_='obj-text')
	#print(obj_atr)
	for p in para:
		if "Object Class:" in p.text:
			cls = True
			ap = p.text
			ap = ap.split(':')[-1]
			ap = ap.strip()
			#print(p.text)
			#print(ap)
			continue
			#print('FOUND IT')
			#quit()
		if cls == True:
			#print('here')
			#strng += p.text + "\n\n"
			strng = ap + "\n"
			break
	
	
	tgs = soup.find('div', {'class': 'page-tags'})
	tgs = tgs.find_all('a')
	#print(tgs)
	temp_string = ''
	for x in tgs:
		if (x.text in class_list) and (cls == False):
			strng = x.text + '\n'
			cls = True
	if cls == False:
		strng = 'NA' + '\n'
		cls = True
	for x in tgs:
		#print(x)
		#print(x.text)
		if '_' not in x.text:
			temp_string += x.text + ' '
	strng += temp_string
	temp_string = ''
	cls = False
	#quit()
	
	return strng


def starter(r):
	print('ATTEMPTING CONTAINMENT: SCP-' + str(r))
	with open("scps/scp-{}.txt".format(r), "w", encoding="utf-8") as f:
		try:
			f.write(getText(r))
			print('SCP-' + str(r) + ' CONTAINMENT COMPLETE.')
		except:
			print(str(r) + ' Not Found.')
				
				
num_proc = 10
pool = Pool(num_proc)
pool.map(starter, rng)




