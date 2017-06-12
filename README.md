## How to use this code
You'll need to load in some sample data by creating a psql database found [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Unzip the file and run `psql -d news -f newsdata.sql` in your terminal app. You'll get three tables, with headers you can find below. Then head into interactive mode with `psql -d news`.

The `logreport.sql` file contains the views you'll want to create in the database to make running this report easier. Copy and paste those in one at a time. Done? Great.

Now, run `python logreport.py` and you'll get a file called `report.txt` with an analytics report of top stories, pageviews by author and days with high 404 error rates.


## Databases

**Articles**
* author: integer
* title: text
* slug: text
* lead: text
* body: text
* time: timestamp with time zone
* id: integer

**Authors**
* name: text
* bio: text
* id: integer

**Log**
* path: text
* ip: inet
* method: text
* status: text
* time: timestamp
* id: integer







