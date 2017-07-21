from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from pprint import pprint

just_the_facts = []

schedule_div_id = "tab-3"

req = Request('http://sfrecpark.org/destination/herz-playground/coffman-pool/', headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(req).read()
soup = BeautifulSoup(page,"html.parser")

# the whole weekly schedule div
sched = soup.find(id=schedule_div_id)

# all the days in order, not guardanteed to start on any particular day
days = sched.find_all('h3')

# all the daily schedule tables
# this doesn't work if some days have no times, thus no table
tables = sched.find_all('table')

if (len(days) != len(tables)):
	pprint("wrong length!")

i = 0 # needed to pull day of the week
for table in tables:
	rows = table.find_all('tr')
	j = 0
	for row in rows:
	    cols = row.find_all('td')
	    cols = [ele.text.strip() for ele in cols]
	    if j > 0: # skip the header row
	    	just_the_facts.append([days[i].get_text(),cols[4],cols[2],cols[3],cols[7]])
	    j=j+1
	i=i+1

pprint(just_the_facts)