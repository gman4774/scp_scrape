
import urllib.request
from bs4 import BeautifulSoup
from multiprocessing import Pool
import sys
import os
import time

class_list = ['safe', 'euclid', 'keter', 'thaumiel', 'neutralized', 'apollyon', 'archon', 'explained', 'pending', 'esoteric-class', 'decomissioned']
area_list  =['12','32','314']
dis_char = '!@'
cls = False
i = 5207
#url = urllib.request.urlopen("http://www.scp-wiki.net/scp-{:03d}".format(i))
url = urllib.request.urlopen("https://scp-wiki.wikidot.com/secure-facilities-locations")

b = url.read()
st = b.decode("UTF-8")
soup = BeautifulSoup(st, 'lxml')#lxml
pageCont = soup.find('div', id="page-content")

a_s = soup.find_all('a')
cur_site = ''
count_scp = 0
full_list = []
lnk = ''
for x in a_s:
	if x.has_attr('href') and 'secure-facility-dossier-' in str(x['href']):
		print(x['href'])
		lnk = (x['href']).split("/")[-1]
		print(lnk)
		#quit()
	if 'site-77'.lower() in x.text.lower():
		print(77)
		lnk = x['href']
		print(lnk)
		print(str(lnk))
		print(x.text)
		print(x)
		
		#time.sleep(2)
		#quit()
	if 'secure-facility-dossier-' in str(lnk):
		print(x.text)
		print('end')
		#quit()
		if 'site-'.lower() in x.text.lower():
			print(x.text)
			#quit()
			cur_site = 'Site-' + ((x.text).split("-", -1)[-1].split()[0])
			if cur_site == 'Site-77':
				print(77)
				#quit()
			#print(cur_site)
			#quit()
		if 'area-'.lower() in x.text.lower():
			cur_site = 'Area-' + ((x.text).split("-", -1)[-1].split()[0])
		print(lnk)
		#quit()
		url = urllib.request.urlopen("https://scp-wiki.wikidot.com/" + lnk)
		b = url.read()
		st = b.decode("UTF-8")
		soup = BeautifulSoup(st, 'lxml')#lxml
		pageCont = soup.find('div', id="page-content")
		a_s_a = soup.find_all('a')
		for y in a_s_a:
			if 'SCP-'.lower() in y.text.lower():
				if '.com' in y.text.lower():
					continue
				cur_scp = 'SCP-' + ((y.text).split("-", 1)[-1].split()[0])
				print('DOSSIER')
				print(cur_site, cur_scp)
				full_list.append((cur_scp, cur_site))
				count_scp += 1
		#
		lnk = ''
		url = urllib.request.urlopen("https://scp-wiki.wikidot.com/secure-facilities-locations")
		b = url.read()
		st = b.decode("UTF-8")
		soup = BeautifulSoup(st, 'lxml')#lxml
		pageCont = soup.find('div', id="page-content")
		
	if 'Site-'.lower() or 'Area-'.lower() in x.text.lower():
		#print(x.text)
		#print((x.text).split("-", 1)[-1].split()[0])
		if 'Site-'.lower() in x.text.lower():
			#print()
			cur_site = 'Site-' + ((x.text).split("-", 1)[-1].split()[0])
		if 'Area-'.lower() in x.text.lower():
			cur_site = 'Area-' + ((x.text).split("-", 1)[-1].split()[0])
		#print(cur_site)
	if 'SCP-'.lower() in x.text.lower():
		if '.com' in x.text.lower():
			continue
		cur_scp = 'SCP-' + ((x.text).split("-", 1)[-1].split()[0])
		print(cur_site, cur_scp)
		full_list.append((cur_scp, cur_site))
		count_scp += 1
	
print(len(full_list))
final_list = []
for x in list(full_list):
	if x not in final_list:
		final_list.append(x)
full_list = final_list
print(len(full_list))

with open("scps/facilities.txt", "w", encoding="utf-8") as f:
	for x in full_list:
		clean_x = str(x)
		for y in dis_char:
			#clean_x = str(x)
			clean_x = clean_x.replace(y, '')
		f.write(str(clean_x) + '\n')
print('CONTAINMENT COMPLETE.')
quit()


				
				

	
