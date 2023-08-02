here is the link ---https://github.com/superdba111/DataStructure/blob/master/smallProject/FAQ/AWS%20PostgreSQL%20RDS.pdf

Partitioning is the process of logically splitting one large table into smaller physical ones. In scenarios where over a period of time, say the size of your PostgreSQL table grows , every operation on that table gets expensive and may lead to serious performance issues. The size of the partition depends on the partition key. The basic idea is when you INSERT or UPDATE on a partitioned table, the database engine routes the data to the appropriate partition (child tables of the main table) and during database query reads, the PostgreSQL optimizer examines the WHERE clause of the query and directs the database scan to only the relevant partitions, thus maintaining the data within the database along with less overall resource utilization.

There are certain considerations to be taken before deciding on implementing partitioning within your database as it involves certain level of complexity. Scenarios where partitioning might be a good fit are as follows:

Table size: There isn’t a hard limit on the table size size as to when you should perform partitioning, however if you encounter longer response times and if the table is larger, then you can consider partitioning.

Table Bloat: Updated and deleted rows result in dead tuples that need to be cleaned up. The vaccum process goes over every row in the table to determine if the space is to be reclaimed or left as is. If the table is big, this process will take a longer time thus resulting in huge resource consumption (CPU). Thus partitioning such tables will help reduce the table scan that needs vaccuming. Say, if we have smaller partitions where some partitions has more changes and some has less, the vaccuum process will clean those with many changes at first, thus resulting in lesser time for the overall vacuum process and more resources available for user access rather than for system maintenance.

Some of the advantages and reasons to incorporate partitioning in your architecture and they are as follows:

High performance framework for large input of data
Faster response time for queries against a partitioned table
Less I/O utilization for maintenance tasks
Before splitting the table, it is important to understad your application’s access patterns. This is the first step before defining partitions and before deciding on the type of partitioning. So, depending on the type of access pattern you can go ahead with a good partitioning strategy most suitable for your application.

Similar to indexing, partitioning startegies rely on targeting the columns (within the WHERE clause or the JOIN conditions) to separate data. With the right type of partitioning, we can achieve good design where the query planner scans small subsets of data rather than the whole large table. Thus, querying few partitions as much as possible.

There are three types of partitioning - RANGE, LIST and HASH and you should select the partitioning typebased on the access patterns of your application. Let’s look at each of them in much more detail.


CREATE TABLE order_details (
order_id integer NOT NULL,
product_id integer,
customer_id integer,
order_status text,
product_quantity integer,
order_date date NOT NULL,
constraint order_details_pk PRIMARY KEY(order_id, order_date)
)PARTITION BY RANGE(order_date);

-- For Q1: Jan’22 to March’22:
CREATE TABLE order_details_Q1 partition of order_details for values from ( '2022-01-01' ) to ( '2022-04-01' );

-- For Q2: April’22 to June’22:
CREATE TABLE order_details_Q2 partition of order_details for values from ( '2022-04-01' ) to ( '2022-07-01' );

-- For Q3: July’22 to Sept’22:
CREATE TABLE order_details_Q3 partition of order_details for values from ( '2022-07-01' ) to ( '2022-10-01' );

-- For Q4: Oct’22 to Dec’22:
CREATE TABLE order_details_Q4 partition of order_details for values from ( '2022-10-01' ) to ( '2023-01-01' );


CREATE TABLE products (
product_id integer NOT NULL,
product_category text,
product_price integer,
constraint products_pk PRIMARY KEY(product_id, product_category)
)PARTITION BY LIST(product_category);

-- For products that fall under the category "Shoes"
CREATE TABLE products_list_shoes partition of products for values IN ('Shoes');

-- For products that fall under the category "Clothing"
CREATE TABLE products_list_clothing partition of products for values IN ('Clothing');

-- For products that fall under the category "Accessories"
CREATE TABLE products_list_accessories partition of products for values IN ('Accessories');

-- For products that fall under the category "Home Essentials"
CREATE TABLE products_list_home_essentials partition of products for values IN ('Home Essentials');


CREATE TABLE customers (
customer_id integer NOT NULL,
customer_name text,
customer_location text,
customer_age integer,
constraint customers_pk PRIMARY KEY(customer_id)
)PARTITION BY HASH(customer_id);


CREATE TABLE customers_hash_p0 partition of customers for values with (modulus 4, remainder 0);

CREATE TABLE customers_hash_p1 partition of customers for values with (modulus 4, remainder 1);

CREATE TABLE customers_hash_p2 partition of customers for values with (modulus 4, remainder 2);

CREATE TABLE customers_hash_p3 partition of customers for values with (modulus 4, remainder 3);

PostgreSQL pg_partman extension is utilized to automate the creation as well as maintenance of partitions. In the previous modules, we looked at how to create partitions manually, howveer in this module we will look at how to automate the same by configuring the pg_partman extension with the following parameters:

Table to be partitioned
Partition type
Partition key
Partition granularity
Partition precreation and management options
Additionally, pg_partman also provides a function run_maintenance_proc that can be called periodically on a scheduled basis to automatically manage partitions (both create as well as drop)

Depending on your partitioning strategy and data access patterns relevant to your business use case, there can be scenarios wherein multi level partitioning is required for improved query performance and good data distribution. Multilevel partitions in PostgreSQL can be created up to infinite level partitions and sub-partitions.

PostgreSQL supports RANGE-RANGE, RANGE-LIST, RANGE-HASH, HASH-HASH, HASH-LIST, HASH-RANGE, LIST-LIST, LIST-RANGE and LIST-HASH which can be created in declarative partitioning.

In this section we will create a RANGE-LIST multi-level partition. Consider the following example with orders table:

Suppose that we first partition the orders table using the RANGE partitioning strategy. Say, we'll partition the orders table on a semi-annual basis using the order_date column.
After creating the first level of partition, let's further divide the semi-annual partitions into smaller partitions based on LIST partitioning strategy. The semi-annual partitions will be further individually sub partitioned based on the list of values in the order_status column (which can be either one of these: Delivered,Returned or Confirmed) of the orders table as shown below.
Thus, achieving multilevel RANGE-LIST partitioning and improving overall query performance in certain scenarios.


