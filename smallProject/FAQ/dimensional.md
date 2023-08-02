Dimensional modeling is a design technique for databases intended to support end-user queries in a data warehouse. It is different from entity-relationship modeling (which is used in OLTP databases) with its emphasis on denormalization and a simpler design to enable faster data retrieval in querying and analytical processes.

Dimensional models are built on two types of tables: fact tables and dimension tables.

1. Fact Tables: Fact tables hold the data to be analyzed, and they contain two types of columns: facts and foreign keys to dimension tables. The facts are typically numerical values that can be aggregated for analysis, such as sales revenue, quantity sold etc.

2. Dimension Tables: Dimension tables provide the context to the facts. They contain details about the facts like date, product, location, etc. They're typically textual fields and are the fields that users want to filter, group, and classify.

Confirmed Dimension Tables:

In dimensional modeling, a confirmed dimension is a dimension that is used across multiple fact tables, i.e., it is shared across different areas of the business. For instance, a 'Date' dimension is typically a confirmed dimension because it can be used in sales, inventory, shipping, HR and almost every business area. Similarly, 'Customer' or 'Product' dimensions may be used across multiple fact tables in a retail business model.

Designing with confirmed dimensions allows for consistent reporting across business areas. For example, the 'Product' dimension would have a consistent definition across the organization whether used in a sales, marketing, or production context.

A key thing to remember when creating confirmed dimensions is to ensure that they are truly identical across all fact tables. If there are discrepancies in the definition of a confirmed dimension across different fact tables, it can lead to confusion and incorrect reports.




