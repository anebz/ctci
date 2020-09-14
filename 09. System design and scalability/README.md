# Chapter 9 System design and scalability

Your goal in these problems is to understand use cases, scope a problem, make reasonable assumptions, create a solid design based on those assumptions, and be open about the weaknesses of your design. Do not expect something perfect.

## Handling the questions

1. Communicate: stay engaged with the interviewer, be open about the issues in the system.
2. Go broad first: don't dive straight into the algorithm part or get excessively focused on one part.
3. Use the whiteboard: use the whiteboard to draw a picture of what you're proposing. helps the interviewer follow your proposed design.
4. Acknowledge interviewer concerns: don't brush off the interviewer's concern, validate them. Acknowledge them and make changes accordingly.
5. Be careful about assumptions
6. State your assumptions explicitly: when you do make assumptions, state them. It allows the interviewer to correct you if you're mistaken, and it shows that you know what assumptions you're making.
7. Estimate when necessary: use other data you know to estimate
8. Drive: talk to your interviewer, ask questions, drive the car. Go deeper, make improvements.

## Design: step-by-step

As an example, your manager might ask you to design a system such as TinyURL.

### 1. Scope the problem

Make sure you're building what the interviewer wants, what specifically you're being asked to implement. Do people create their own short URLs, is it auto-generated, do we keep track of stats, does the URL stay alive forever? Make a list of the major features or use cases:

* Shortening a URL into a TinyURL
* Analytics for a URL
* Retrieving the URL associated with a TinyURL
* User accounts and link management

### 2. Make reasonable assumptions

Don't assume you will only deal with 100 users per day, or that you have unlimited memory available. But you can assume you will have a max of one million URLs per day, and you can estimate how much data your system might have to store.

Some assumptions need some "product sense". It is not advantageous that links are only ready after 10mins, users will want the link to be available immediately. But it is ok for stats to take 10mins to load.

### 3. Draw the major components

Go to the whiteboard, draw a diagram of the major components. You might need a frontend server that pull data from the backend's data store. You might have other servers that crawl the internet for some data, and another that process analytics. Draw a picture of what this system might look like. Walk through the system from end-to-end to provide a flow.

### 4. Identify the key issues

What are the bottlenecks or major challenges of the system. Some links might be accessed frequently, but others can suddenly peak. You don't necessarily want to constantly hit the database. The interviewer might provide some guidance, use it.

### 5. Redesign for the key issues

Adjust the system for the key issues. Stay up at the whiteboard and update the diagram. Be open about limitations in your design.

## Algorithms that scale: step-by-step

Sometimes you are asked to design an algorithm, but in a scalable way.

1. Ask questions: the interviewer might have left out details, intentionally or unintentionally.
2. Make believe: pretend that the data fits on one machine and there are no memory limitations. Then fix the problem.
3. Get real: how much data can you store in one machine, and what problems occur when you split the data? How do you logically divide the data, and how does one machine identify where to look up a difference piece of data.
4. Solve problems: think how to solve the issues identified in step 3: the solution for one issue might be to remove the issue entirely, it simpliy mitigate the issue. Work iteratively, once you have solved the problems from step 3, tackle the new problems..

## Key concepts

> Horizontal vs. vertical scaling

* Vertical scaling: increasing the resources of a specific node, for example add additional memory to a server to improve its ability to handle load changes.
* Horizontal scaling: increase the number of nodes. Add more servers, decreasing the load of individual servers.

> Load balancer

Typically some frontend parts of a scalable website are thrown behind a load balancer, allowing the system to distribute the load evenly so that one server doesn't crash and take down the whole system. To do this, you need a network of cloned servers that all have the same code and access to the same data.

> Database denormalization and NoSQL

Joins in a relational databaset such as SQL can get very slow when the system is bigger. For this reason, you would generally avoid them. Denormalization is one part of this. Means adding redundant information into a db to speed up reads. Add different tables with redundant information.

You can also go with a NoSQL db, which does not suppor joins and structures data in a different way. It is designed to scale better.

> Database partitioning, sharding

It means splitting the data across multiple machines while ensuring you know which data is on which machine.

* Vertical partitioning: partitioning by feature. If you are building a social network, you can have one partition for tables related to profiles, another for messages. If one table gets very large, you might need to repartition that database.
* Key-based / hash-based partitioning: it uses some part of the data (an ID for example) to partition. For example, allocate N servers and put the data on mod(key, n). But the number of servers must be fixed. Adding new servers means reallocating the data, which is very expensive.
* Directory-based partitioning: you maintain a lookup table for where the data can be found. You can add new servers easily, but the lookup table can be a single point of failure. And constantly accessing this table impacts performance.

> Caching

An in-memory cache can deliver very fast results, you pair keys to values and it typically sits between the application layer and the data store. When an app requests a piece of information, it first tries the cache. If the cache does not contain the key, it looks it up in the data store. When you cache, you can cache a query and its result directly, or you can cache the specific object.

> Asynchronous processing and queues

Slow operations should ideally be done asynchronously, otherwise the user might get stuck waiting for a process to complete. Sometimes this can be done in advance, preprocessing. If we are running a forum, we should re-render a page that lists the most popular posts and the number of comments. The list might be slightly out of date, but that is better than a user stuck waiting on the website to load simply because someone added a new comment and invalidated the cached version of this page.

> Networking metrics

* Bandwidth: the maximum amount of data that can be transferred in a unit of time in the best conditions (bits/s, gbyte/s)
* Throughput: the actual amount of data that is transferred
* Latency: how long it takes the data to go from one end to the other. The delay between a user sending information and the receiver receiving it

> MapReduce

A MapReduce program is used to process large amounts of data. It requires a map step and a reduce step See more in page 642 of book.

* Map step: takes data and creates a <key, value\> pair
* Reduce step takes a key and a set of associated values and 'reduces' them in some way, emitting a new key and value

## Considerations

* Failures: any part of the system can fail, plan accordingly
* Availability and reliability: av: percentage of time the system is operational. Re: probability that the system is operational for a certain unit of time
* Read-heavy vs. write-heavy: if an application will read many times, you could queue up the writes (think about potential failure). If it is read-heavy, cache
* Security: think about security issues and design around those

See example problem in page 143 in book.