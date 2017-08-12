from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json
import pandas

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

pool_schedules = []

# magic strings
schedule_div_id = "tab-3"
no_classes = "There are no Classes at this time"

def scrape(pool):
	req = Request(pool_pages[pool], headers={'User-Agent': 'Mozilla/5.0'})
	page = urlopen(req).read()
	soup = BeautifulSoup(page,"html.parser")

	# the whole weekly schedule div
	sched = soup.find(id=schedule_div_id)

	# all the days in order, not guardanteed to start on any particular day
	days = sched.find_all('h3')

	# look at each day
	for day in days:
		day_name = day.string.strip()
		for sibling in day.next_siblings:
			# found the no_classes text, so break out of this day
			if sibling.string == no_classes:
				break

			# find the schedule table
			if sibling.name == "table":
				rows = sibling.find_all('tr')
				for row in rows:
					cols = row.find_all('td')
					cols = [ele.text.strip() for ele in cols]
					if len(cols) > 0:
						pool_schedules.append((pool,day_name,cols[0].strip(),cols[1].strip(),cols[2].strip()))

				# only one schedule table per day, so leave this day now
				break

if __name__ == "__main__":
    for k in pool_pages.keys():
	    scrape(k)
    
    #with open('data.json', 'w') as outfile:
	#    json.dump(pool_schedules, outfile)

    pools_dataframe = pandas.DataFrame(pool_schedules, columns=['pool', 'day', 'class', 'start', 'end'])
    pools_dataframe.to_csv('data.csv', index=False, encoding='utf-8')  

