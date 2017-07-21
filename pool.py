from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from pprint import pprint

pool_pages = {
'balboa':'http://sfrecpark.org/destination/balboa-park/balboa-pool/',
'coffman':'http://sfrecpark.org/destination/herz-playground/coffman-pool/',
'garfield':'http://sfrecpark.org/destination/garfield-square/garfield-pool/',
'hamilton':'http://sfrecpark.org/destination/hamilton-rec-center/hamilton-pool/',
'mlk':'http://sfrecpark.org/destination/bay-view-playground/martin-luther-king-jr-pool/',
'mission':'http://sfrecpark.org/destination/mission-playground/mission-community-pool/',
'north beach':'http://sfrecpark.org/destination/joe-dimaggio-playground/north-beach-pool/',
'rossi':'http://sfrecpark.org/destination/angelo-j-rossi-playground/rossi-community-pool/',
'sava':'http://sfrecpark.org/destination/carl-larsen-park/sava-pool/'
}

just_the_facts = []
schedule_div_id = "tab-3"
no_classes = "There are no Classes at this time"

req = Request(pool_pages['coffman'], headers={'User-Agent': 'Mozilla/5.0'})
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
		# found the no_classes text, so break out of this day
		if sibling.string == no_classes:
			just_the_facts.append([day_name,'no classes'])
			break

		# find the schedule table
		if sibling.name == "table":
			rows = sibling.find_all('tr')
			for row in rows:
				cols = row.find_all('td')
				cols = [ele.text.strip() for ele in cols]
				if len(cols) > 0: 
					# sometimes the name of the activity, cols[0], has an
					# odd bit of stuff outside the quotes. See coffman pool
					# for an example. When using pprint it causes extra line breaks.
					just_the_facts.append([day_name,cols[0],cols[1],cols[2]])

			# only one schedule table per day, so leave this day now
			break

pprint(just_the_facts)