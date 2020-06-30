## Setting Up Environment

It is recommended to create a virtual environment to setup the project.

Tools like [virtualenv](https://virtualenv.pypa.io/en/latest/) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) provide isolated Python environments, which are cleaner than installing packages systemwide (as they prevent dependency conflicts). They also let you install packages without root privileges.

### For Ubuntu or Mac
Create a new virtual environment by choosing a Python interpreter and making a  `./venv`  directory to hold it:

    $ python3 -m venv  ./venv

Activate the virtual environment:

    $ source ./venv/bin/activate

### For Windows
Set up is not tested for Windows. Need to test and update the steps here appropriately.

### Install dependencies
Install the packages using the following command:

    pip install -r requirements.txt


## Running the Crawlers
Following are the spiders that are part of cbfc

1. movies
2. movies_patch

Execute the following commands from the root folder to run the crawler:

    cd cbfc

To run the crawler for a default year (2018):

    scrapy crawl movies

To run the crawler for a specific year, 2017 for eg:

    scrapy crawl movies -a from_date=1992 -a to_date=1993