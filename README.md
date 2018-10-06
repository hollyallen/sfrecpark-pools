# sfrecpark-pools
This is a tool for deciding when to swim at [San Francisco public pools](http://sfrecpark.org/recreation-community-services/aquatics-pools/).

First run generate.py to gather pool swim times from [sfrecpark.org](http://sfrecpark.org) and output the html file index.html. This page contains all the data and provides some simple filtering.

You could then run a local web server (for example 'python -m SimpleHTTPServer 8000') to serve up the
html and javascript. The most recent version is also served at https://s3.amazonaws.com/sfrec.info/index.html

## Getting Started

### Prerequisites

To run the python script you'll need [Python 3.x](https://www.python.org/downloads/) and 
[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/).

