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

movies

To run the crawler

    scrapy crawl movies -a from_date=01/01/1950 -a to_date=12/31/1951 -o list.json

movies_patch

put all the missed entries into `data/missed.json` then run below command

    scrapy crawl movies_patch -o patch_list.json
