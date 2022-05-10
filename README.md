# SCP Scraper Project Part 1

I was never able to find a full list of all SCP's from the scp-wiki, so I decided to put something together.

In later parts, I will clean the data, inspect it, and once everything is as it should be,  put it into sql server. 

I plan on also doing this for the international branches of the SCP wiki's.

The code here is all python3 and the files have different functions.

* **scp_scrape.py** Using BeautifulSoup it scrapes for all SCP's 2-10,000. This file also uses multiprocessing to run multiple scrape jobs at once in order to speed things up. This file will still pull the data if there is an '18+ warning, click to continue'.
* **scp001.py** Since SCP-001 has multiple proposals, a separate script was written for it. does not use multiprocessing.
* **fac.py** This file accesses https://scp-wiki.wikidot.com/secure-facilities-locations to get as many SCP's site locations. It scrapes all sites, areas, and SCP's associated with them. This file does not use multiprocessing.
* **combo.py** The other files created individual files for each SCP and the locations. This file combines everything and spits out a CSV file. 


## NOTE:
The data from this is currently not correct, I still need to analyze my code and see where the problems are.

It appears to only be the facility association with the SCP's, some are incorrect.
