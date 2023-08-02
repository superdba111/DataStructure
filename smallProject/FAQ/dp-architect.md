AWS general architecture info links

https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/reference-architecture.html

https://wellarchitectedlabs.com/operational-excellence/

https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/database-architecture-selection.html?dbd_mod2

MongoDB and PostgreSQL are fundamentally different types of databases, MongoDB being a NoSQL document-based database and PostgreSQL being a SQL-based relational database. Therefore, their schema design principles are quite different.

Schema Structure

MongoDB: MongoDB is schema-less, meaning the structure of documents in a collection does not need to be defined in advance and can vary. For example, one document in a collection could have completely different fields from another. This allows a high degree of flexibility, but it also means that you need to handle data consistency in your application code.

PostgreSQL: In PostgreSQL, the schema needs to be defined before inserting data. A table in PostgreSQL requires a pre-defined structure with specified columns and data types. This ensures a high degree of data consistency, as data must fit the defined schema.

Data Model

MongoDB: MongoDB uses a document model, which can embed nested data in a single document. This can often align more directly with objects in application code and can allow for more efficient data retrieval.

PostgreSQL: PostgreSQL uses a relational model, where data is stored in tables and rows, and relationships between data are stored in terms of primary and foreign keys.

Denormalization vs Normalization

MongoDB: MongoDB allows for data denormalization. You can store related data in a single document, which can make queries more efficient because all the necessary data can be retrieved in a single operation. However, this can also lead to data redundancy and inconsistency if not managed carefully.

PostgreSQL: PostgreSQL encourages data normalization, where data is split into multiple tables and relationships are maintained using primary and foreign keys. This reduces data redundancy and helps maintain data consistency, but it can also make queries more complex because you need to join multiple tables together.

Scaling

MongoDB: MongoDB supports horizontal scaling through sharding, which distributes data across multiple servers. This can make it easier to increase capacity as demand grows.

PostgreSQL: PostgreSQL traditionally supports vertical scaling, i.e., adding more resources to a single server. However, with extensions and additional tools, horizontal scaling can also be achieved in PostgreSQL.

Transactions

MongoDB: As of version 4.0, MongoDB supports multi-document transactions, but the use of transactions can have a performance impact.

PostgreSQL: PostgreSQL has full ACID compliance, making it a better option for use cases that require complex transactions, such as financial applications.

In conclusion, the choice between MongoDB and PostgreSQL for a project depends on the specific requirements, such as the structure of the data, the scale of the data, the nature of queries, and the need for transactions. Each has its strengths and is better suited to different kinds of applications.

Designing an Apache Cassandra or AWS Keyspaces (a managed Cassandra-compatible database service by AWS) data model requires a unique approach as compared to traditional relational databases. Cassandra uses a wide column store model where rows are organized into tables, but the structure of the rows doesn't need to be uniform. Here are some best practices for designing a Cassandra schema:

1. Understand Your Queries First:
Unlike in a relational database, you can't easily join tables in Cassandra, and there is no equivalent to a SQL "WHERE" clause. Cassandra is optimized for high-speed read operations and you typically design your schema around the queries you'll be performing, rather than normalizing data as you would in a relational database.

2. Denormalization and Redundancy is Acceptable:
Cassandra encourages denormalization; storing the same data in multiple tables is common because it can make read queries more efficient. It's not uncommon to create a new table just to handle a specific type of query.

3. Minimize the Number of Partitions Read:
Cassandra's data distribution design relies on partitioning. Data in Cassandra is distributed across nodes in a cluster by partition key, which is defined by the primary key of the table. The more partitions read, the slower the query, so it's important to model your data to reduce the number of partitions accessed.

4. Use Time Series Data Modeling:
Cassandra excels at time series data modelling. In such cases, it's common to use a compound primary key with a partition key (e.g., device_id) and one or several clustering columns (e.g., event_time).

5. Be Careful with Counters:
Counter tables in Cassandra can be a source of performance problems and are best avoided if possible. Consider using them only when necessary.

6. Use Appropriate Compaction Strategy:
Cassandra provides different compaction strategies like SizeTieredCompactionStrategy (STCS), LeveledCompactionStrategy (LCS), and TimeWindowCompactionStrategy (TWCS). Choose the one that best suits your use case and access pattern.

7. Consider Your Consistency Requirements:
Cassandra provides tunable consistency. For a write, you could specify that you want to write to at least one node, a quorum of nodes, all nodes, etc. If you require strong consistency, you can achieve that with Cassandra, but at a cost to availability.

Time series data is a series of data points ordered in time, typically in equally spaced intervals. It's widely used in many areas such as stock prices, climate modeling, energy usage, sales forecasting, and more. Designing a database schema for time-series data can be challenging because of the high volume and velocity of such data.

In a time-series database, the key design goal is to optimize for fast data ingestion and querying of time-ordered data. You often store each event as it happens and include a timestamp with it.

Here are some general principles for time series data modeling:

1. Use Appropriate Data Structures: In a time-series data model, you would typically use a time-stamp as a key, and the measured event as a value. Therefore, it's ideal to use a database that offers data structures that are optimized for such data, such as wide-column stores (like Cassandra), or specialized time-series databases like InfluxDB or TimescaleDB.

2. Granularity of Data: The granularity of data depends on the precision of the timestamps you are recording. If the intervals are small, you'll have a lot of data points, and therefore, you need to design your schema to handle this high volume of data.

3. Aggregations and Rollups: For time-series data, aggregations and rollups are quite common. These involve summarizing data for large time intervals for analytical queries. Design your schema to facilitate these operations efficiently.

4. Data Retention: Often, you'll need to delete older time-series data that's no longer needed to free up space. Design your schema to make deletion of old data efficient and to minimize its impact on performance.

5. Partitioning and Sharding: Due to the large volume of time-series data, it's often necessary to distribute data across multiple nodes or servers. This can improve write and read throughput and make data management more manageable.

6. Indexing: Indexes are essential for efficiently querying time-series data. In most cases, you'll want an index on the timestamp column to enable fast range queries. Some databases automatically index the timestamp.

As an example, if you're using a database like Cassandra to store time-series data, you might have a schema that looks something like this:

CREATE TABLE sensor_data (
    sensor_id text,
    event_time timestamp,
    reading float,
    PRIMARY KEY (sensor_id, event_time)
) WITH CLUSTERING ORDER BY (event_time DESC);
In this example, sensor_id is the partition key, and event_time is the clustering key. This design allows efficient writes of new sensor data, and efficient range queries of sensor data over a particular time period.

Remember, time series data modeling is complex and depends heavily on your specific use case. Always benchmark and test your data model with realistic data and queries to ensure it meets your requirements.

The document model is a type of non-relational (NoSQL) database model that is designed to store, retrieve, and manage document-oriented information. It is a semi-structured model that can store data of any type, like JSON, XML, BSON, etc.

Designing a document model involves creating "documents" that contain all the information about a particular item. This can include nested data, and there is no need for a predefined schema. The data can be structured in the best way to support the application's access patterns.

Here are some best practices for designing a document model:

1. Embedding:
The first rule in the document model is to embed data in a single document whenever possible. Embedding makes reading and writing data more efficient because you only need to perform one operation on the database.

For example, if you were storing data about books, you might design your documents like this in MongoDB:


{
    "_id": "1",
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "published_year": 1925,
    "reviews": [
        {
            "user": "John",
            "rating": 5,
            "text": "A masterpiece"
        },
        {
            "user": "Jane",
            "rating": 4,
            "text": "Really enjoyed it"
        }
    ]
}
In this example, each book has a list of reviews embedded within it. This makes it possible to retrieve all information about a book and its reviews in a single query.

2. Document size considerations:
Document databases typically have a maximum document size (e.g., 16MB for MongoDB). If your data is larger than this, you will need to split it into multiple documents. However, in practice, this limit is rarely reached unless you are storing very large amounts of data in a single document.

3. Indexing:
Indexing in a document database is similar to indexing in a relational database, and it's important to create indexes for any fields you will be querying often to speed up read operations.

4. Avoid large arrays:
While it is possible to store arrays in a document, large, unbounded arrays can cause performance issues. If an array is expected to grow without limit, consider a different data model.

5. Denormalization:
Unlike relational databases, document databases encourage denormalization. This means you can (and often should) duplicate data in your documents to optimize read performance. However, denormalization can make updates more complex since you need to update data in multiple places.

6. Use the right data types:
Most document databases support rich data types (e.g., dates, timestamps, geospatial data). Use these data types whenever possible as they can provide additional functionality and improve query performance.

In conclusion, the document model is highly flexible and works well when data can be grouped together into documents that align well with your application's data access patterns. However, it may not be a good fit for all use cases, particularly those requiring complex joins or transactions across multiple entities.






