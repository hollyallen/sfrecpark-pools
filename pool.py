from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from pprint import pprint

just_the_facts = []

schedule_div_id = "tab-3"
no_classes = "There are no Classes at this time"

#req = Request('http://sfrecpark.org/destination/herz-playground/coffman-pool/', headers={'User-Agent': 'Mozilla/5.0'})
#req = Request('http://sfrecpark.org/destination/balboa-park/balboa-pool/', headers={'User-Agent': 'Mozilla/5.0'})
req = Request('http://sfrecpark.org/destination/bay-view-playground/martin-luther-king-jr-pool/', headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(req).read()
soup = BeautifulSoup(page,"html.parser")

# the whole weekly schedule div
sched = soup.find(id=schedule_div_id)

# all the days in order, not guardanteed to start on any particular day
days = sched.find_all('h3')

# look at each day
for day in days:
	day_name = day.string
	for sibling in day.next_siblings:
		# looking for either a table or p
		if sibling.name == "table":
			rows = sibling.find_all('tr')
			j = 0
			for row in rows:
			    cols = row.find_all('td')
			    cols = [ele.text.strip() for ele in cols]
			    if j > 0: # skip the header row
			    	just_the_facts.append([day_name,cols[5],cols[1],cols[2]])
			    j=j+1
		if sibling.string == no_classes:
			break


pprint(just_the_facts)