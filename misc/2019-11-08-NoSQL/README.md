Welcome
-------

This is a presentation about NoSQL for cartographers.

Why me?
-------

- 2008: first paid software job.
- 2012: graduated Computing Science.
- 2014-2016: Amazon Web Services.
- 2016+: Uber.
- Using SQL and NoSQL at dayjob.

What is a server?
-----------------

SQL
---

- Invented > 50 years ago.
- Technologies differ, concepts are the same.

Power and limitation of SQL
---------------------------

Let's model a house on a piece of land.

- There will be always a piece of land under a house.
- SQL says you can enforce this.

**They must be on the same server to enforce this constraint.**

If constraint cannot be created, it's not SQL.
If it's SQL, all houses and all areas must be on the same server.

Get a big database
------------------

$30 to about a $1M. Show graphics.

Alternatives
============

Cat videos do not require topology. But we still need storage -- No SQL!

Like-SQL
--------

Forego some SQL constraints, but use the same (/similar) language:
- No uniqueness constraints.
- No foreign keys.
- ... many more restrictions.

Hive:
```
SELECT a.foo FROM invites a WHERE a.ds='2008-08-15';
```


Key-Value: fast & small
-----------------------

DynamoDB, Cassandra. Some have their language, some don't.

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

Cassandra:
```
INSERT INTO monkeys (type, family, common_name, conservation_status)
VALUES ('New World Monkey', 'Cebidae', 'white-headed capuchin', 'Least concern');
```

Key-Value: slow & big
---------------------

S3.

https://www.youtube.com/watch?v=8vQmTZTq7nw
