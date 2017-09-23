from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import datetime

pool_pages = {
'Balboa':'http://sfrecpark.org/destination/balboa-park/balboa-pool/',
'Coffman':'http://sfrecpark.org/destination/herz-playground/coffman-pool/',
'Garfield':'http://sfrecpark.org/destination/garfield-square/garfield-pool/',
'Hamilton':'http://sfrecpark.org/destination/hamilton-rec-center/hamilton-pool/',
'MLK':'http://sfrecpark.org/destination/bay-view-playground/martin-luther-king-jr-pool/',
'Mission':'http://sfrecpark.org/destination/mission-playground/mission-community-pool/',
'North Beach':'http://sfrecpark.org/destination/joe-dimaggio-playground/north-beach-pool/',
'Rossi':'http://sfrecpark.org/destination/angelo-j-rossi-playground/rossi-community-pool/',
'Sava':'http://sfrecpark.org/destination/carl-larsen-park/sava-pool/'
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

def make_page():
	html = "<!DOCTYPE html>"
	html += "<html><head><title>Pool Tool</title>"
	html += "<link rel=\"stylesheet\" type=\"text/css\" href=\"./style.css\">"
	html += "<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js\"></script>"
	html += "<script src=\"./script.js\"></script></head>"
	html += "<body><h1>Pool Tool When Swim?</h1>"
	html += "<p><img src=\"pool_map.png\" height=500></p>"	
	html += "<p>Pool times were current as of "
	html += datetime.datetime.now().strftime("%-I:%M %p on %A %B %d, %Y")
	html += "</p>"	
	html += "<p>I'd like to swim at "
	html += "<input type=\"text\" id=\"inputPool\" onkeyup=\"searchPool()\" placeholder=\"pool name\">"
	html += " on "
	html += "<input type=\"text\" id=\"inputDay\" onkeyup=\"searchDay()\" placeholder=\"day\">"
	html += " when the swimming type is "
	html += "<input type=\"text\" id=\"inputClass\" onkeyup=\"searchClass()\" placeholder=\"swimming type\">"
	html += "<p>"
	html += "<table id=\"poolTable\">"
	html += "<tbody><tr><th>Pool Name</th><th>Day</th><th>Swimming Type</th><th>Start Time</th><th>End Time</th></tr>"

	# each row in table
	for class_time in pool_schedules:
		html += "<tr>"
		for elem in class_time:
			html += "<td>"
			html += elem
			html += "</td>"
		html += "</tr>"

	html += "</table></body></html>"

	return html

if __name__ == "__main__":
    for k in pool_pages.keys():
        scrape(k)

    html = make_page()
    with open("index.html","w") as file:
        file.write(html)


