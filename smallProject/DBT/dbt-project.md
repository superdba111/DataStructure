## see LAB snowflake dbt file structure at first
in dbt, folder almost = DAG, preserve a narrowing DAG up to the marts layer

### Staging — creating our atoms, our initial modular building blocks, from source data
✅ Renaming
✅ Type casting
✅ Basic computations (e.g. cents to dollars)
✅ Categorizing (using conditional logic to group values into buckets or booleans, such as in the case when statements above)
❌ Joins 
❌ Aggregations
✅ Materialized as views

### Intermediate — stacking layers of logic with clear and specific purposes to prepare our staging models to join into the entities we want
✅ Subdirectories based on business groupings
❌ Exposed to end users
✅ Materialized ephemerally
✅ Materialized as views in a custom schema with special permissions
✅ Structural simplification
✅ Re-graining
✅ Isolating complex operations

### Marts — bringing together our modular pieces into a wide, rich vision of the entities our organization cares about
✅ Group by department or area of concern
✅ Name by entity
❌ Build the same concept differently for different teams
✅ Materialized as tables or incremental models
✅ Wide and denormalized
❌ Too many joins in one mart
✅ Build on separate marts thoughtfully

### YAML config file in DBT
✅ Config per folder
❌ Config per project
⚠️ Config per model
✅ Cascade configs

### other folders
✅ seeds for lookup tables
❌ seeds for loading source data
✅ analyses for storing auditing queries
✅ tests for testing multiple specific tables simultaneously
✅ snapshots for SCD 
✅ macros for DRY-ing up transformations you find yourself doing repeatedly
