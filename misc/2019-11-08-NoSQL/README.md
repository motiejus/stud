Welcome
-------

NoSQL for cartographers.


Motiejus Jakštys

2019-11-08








Why me?
-------

- 2008: first paid software job.
- 2009-2012: graduated Computing Science in Glasgow.
- 2014-2016: job: Amazon Web Services.
- 2016-now:  job: Uber.

SQL and NoSQL are part of the job.








What is a server?
-----------------

Demonstration.

- pi
- pi-at-home.jpg










SQL
---

- Invented > 50 years ago.
- Technologies change, concepts remain.











Power and limitation of SQL
---------------------------

Let's model a house on a piece of land.

- There will be always a piece of land under a house.
- SQL says you can enforce this.

**They must be on the same server to enforce this constraint.**


What do we do?




Get a big database
------------------

$30 to about a $1M.












Alternatives
============

Split data across many servers!

Topology is not always needed:
- Pictures/videos.
- Stock prices.
- Sensor measurements.


Hey, No SQL!







Sort-of-SQL
-----------

Leave the syntax, cut out constraints.
- familiar syntax.
- more storage.
- less features.

Hive:
```
SELECT a.foo FROM invites a WHERE a.ds='2008-08-15';
```






Key-Value: fast & small
-----------------------

- Different syntax
- Different features

DynamoDB:
```
table = dynamodb.create_table(
    TableName='users',
    KeySchema=[
        { 'AttributeName': 'username', 'KeyType': 'HASH' },
        { 'AttributeName': 'last_name', 'KeyType': 'RANGE' }
    ],
)
```





Key-Value: slow & very big
---------------------

Videos or just large files? S3 is most popular.

Imaginge an infinite disk.











Cloud
-----

"The Cloud" is just someone's servers with software.

- pi-datacenter.jpg
- datacenter.jpg
- snowball-edge.jpg












Storage
-------

Storage in "the cloud" is quite cheap. People start moving.

https://www.youtube.com/watch?v=8vQmTZTq7nw
