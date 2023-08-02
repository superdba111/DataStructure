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
