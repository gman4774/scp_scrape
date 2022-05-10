import csv
import urllib.request
from bs4 import BeautifulSoup
from multiprocessing import Pool
import sys
import os
import time

f_d = {}
path = 'scps'
os.chdir(path)
 
def read_text_file(path):
	with open(path, 'r') as f:
		#print(f.read())
		if path in f_d:
			print('DUPLICATE')
			#quit()
		else:
			temp_t = f.readlines()
			t2 = []
			for y in list(temp_t):
				#print(y)
				t2.append(y.replace('\n', ''))
				#print(t2)
				#quit()
			
			f_d[path.replace('.txt', '')] = (t2)
	#print(f_d)
	#quit()

for file in os.listdir():
	print(file)
	if file.endswith(".txt") and file.startswith('scp-'):
		file_path = f"{path}/{file}"
		#print(file)
		#print(file_path)
		#quit()
		#read_text_file(file_path)
		read_text_file(file)


with open('facilities.txt', 'r') as g:
	all_site = g.readlines()
	for x in f_d:
		for y in all_site:
			#print(x)
			#print(y)
			#print(x in y.lower())
			#print(y.lower())
			y = y.replace("'", '')
			y = y.replace("(", '')
			y = y.replace(")", '')
			y = y.replace(" ", '')
			y = y.replace("\n", '')
			
			y = y.lower()
			j = y.split(',')
			#print('J')
			#print(j)
			#for a in j:
			#	print(a)
			#quit()
			if x == j[0]:
				
				f_d[x] += [j[1]]
				#print(x)
				#print(f_d[x])
				#quit()
				break
for x in f_d:
	print(x)
	print(f_d[x])
	#for b in f_d[x]:
	#	print(b)
	#quit()
print(len(f_d))

new_row = []

with open('data2.csv', 'w') as f:
	write = csv.writer(f)
	for key in f_d.keys():
		new_row.append(key)
		for b in f_d[key]:
			print(b)
			new_row.append(b)
		write.writerow(new_row)
		new_row = []
		
		#f.write("%s,%s\n"%(key,f_d[key]))
		
		
		
		
