# sfrecpark-pools
This is a tool for deciding when to swim at [San Francisco public pools](http://sfrecpark.org/recreation-community-services/aquatics-pools/).

First run the web scraper, pool.py, to gather pool swim times from [sfrecpark.org](http://sfrecpark.org) webpages. 

Then run a local web server (for example 'python -m SimpleHTTPServer 8000') to serve up the
html and javascript. This page reads the csv file and provides some simple filtering.

## Getting Started

### Prerequisites

To run the python script you'll need [Python 3.x](https://www.python.org/downloads/),
[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/), and 
[Pandas](http://pandas.pydata.org/).

To run the webpage you'll need a local copy of the [Papaparse](http://papaparse.com/)
library (minified version) to parse the csv file that you python script created.

