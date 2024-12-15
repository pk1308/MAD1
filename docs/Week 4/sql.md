# SQL

**Summary**
**Relational Databases**

Relational databases, developed by IBM in the 1970s, are a type of data storage organized in tabular format. They consist of tables, which have columns (fields) and rows (individual entries). Each table represents a specific entity or category of data, such as students, courses, or departments.

**Key Fields**

A key field is a unique identifier for each row in a table. The primary key is the most important key field, allowing for fast and efficient access to data, especially in large databases. Foreign keys, on the other hand, are used to establish relationships between different tables, linking related data.

**Queries**

Queries are used to retrieve data from a database based on specific criteria. They are written in a structured language called SQL (Structured Query Language), which uses English-like syntax but has a specific format. Queries can be used to find specific records, filter data based on conditions, or perform mathematical operations.

**Structured Query Language (SQL)**

SQL is a verbose language that enables users to interact with relational databases. Its syntax includes keywords, operators, and clauses that specify the desired data manipulation or retrieval operations. SQL consists of several specific types of operations, including:

* **Select:** Retrieves specific columns or rows from a table
* **From:** Specifies the table(s) to retrieve data from
* **Where:** Filters the data based on specified conditions
* **Join:** Combines data from multiple tables based on matching key fields

**Inner Join**

An inner join operation combines rows from two or more tables based on common key fields. It retrieves only the rows that match in both tables, resulting in a smaller dataset that contains only the relevant data.

**Cartesian Product**

A Cartesian product is a theoretical operation that combines all rows from two or more tables, resulting in a much larger dataset. However, in practice, it is uncommon to use Cartesian products due to the large number of unnecessary combinations.

**Query Example: Finding Students Enrolled in Calculus**

The following SQL query demonstrates how to find all students enrolled in a course named "Calculus":

```sql
SELECT s.name
FROM Students s
JOIN StudentsCourses sc ON s.IDNumber = sc.studentID
JOIN Courses c ON c.ID = sc.courseID
WHERE c.name = 'Calculus';
```

In this query:

* The SELECT clause specifies the column to be retrieved (student names).
* The FROM clause specifies the tables to be joined (Students, StudentsCourses, and Courses).
* The JOIN clauses specify how the tables are to be joined based on the IDNumber field (studentID and courseID).
* The WHERE clause filters the results to include only students enrolled in the "Calculus" course.

**Summary**

Relational databases provide a structured and efficient way to store and manage data in a tabular format. They use keys and relationships to organize and connect data. SQL is a specific language used to interact with relational databases, allowing users to retrieve and manipulate data based on specific criteria.

# ACID properties

ACID properties are a set of principles that ensure reliable processing of database transactions. The acronym ACID stands for Atomicity, Consistency, Isolation, and Durability. Each of these properties contributes to the reliability and robustness of database systems, particularly in multi-user and distributed environments.

### 1. Atomicity

- **Definition**: Ensures that each transaction is treated as a single "unit," which either completes in its entirety or not at all.
- **Key Point**: If any part of the transaction fails, the entire transaction fails, and the database state is left unchanged.
- **Example**: In a banking system, a transaction transferring money from one account to another will either fully complete (debiting one account and crediting another) or not occur at all.

### 2. Consistency

- **Definition**: Ensures that a transaction brings the database from one valid state to another valid state, maintaining all predefined rules, such as constraints, cascades, and triggers.
- **Key Point**: Any data written to the database must be valid according to all defined rules, including integrity constraints.
- **Example**: After a transaction, all database invariants, such as foreign key constraints or unique constraints, must be satisfied.

### 3. Isolation

- **Definition**: Ensures that the concurrent execution of transactions leaves the database in the same state that would have been obtained if the transactions were executed sequentially.
- **Key Point**: Transactions are isolated from each other; intermediate results of a transaction are not visible to other transactions until the transaction is committed.
- **Example**: If two users are concurrently trying to update the same data, the isolation property ensures that one transaction is completed before the other begins, preventing data corruption.

### 4. Durability

- **Definition**: Ensures that once a transaction has been committed, it will remain so, even in the event of a system failure.
- **Key Point**: Changes made by committed transactions are permanently recorded in the database and must survive any subsequent failures.
- **Example**: After a successful transaction, such as a completed purchase order, the data should persist even if the system crashes immediately afterward.

### Detailed Examples

#### Atomicity Example

Consider a transaction that involves transferring $100 from Alice's account to Bob's account. The transaction involves two steps:

1. Deduct $100 from Alice's account.
2. Add $100 to Bob's account.

If the system crashes after step 1 but before step 2, atomicity ensures that Alice's account will not be debited unless Bob's account is credited. The transaction will be rolled back, and Alice's account will remain unchanged.

#### Consistency Example

Suppose a database rule states that the balance of any account should never be negative. If a transaction attempts to transfer more money than the available balance in an account, the transaction will fail, maintaining consistency.

#### Isolation Example

Two transactions occur simultaneously:

- Transaction A: Withdraws $50 from Account 1.
- Transaction B: Transfers $30 from Account 1 to Account 2.

Isolation ensures that the transactions do not interfere with each other. One transaction will complete before the other starts, ensuring that Account 1's balance is correctly updated and not affected by the concurrent transaction.

#### Durability Example

A transaction records the sale of a product. Once the transaction is committed, the sale information is stored in the database. Even if the system crashes immediately after the transaction commits, the sale information remains recorded, ensuring data is not lost.

### Importance of ACID Properties

- **Reliability**: Ensures the database reliably handles transactions, even in the event of errors, system crashes, or power failures.
- **Data Integrity**: Maintains data integrity by ensuring transactions are processed in a reliable and consistent manner.
- **Concurrent Access**: Manages concurrent access by multiple users, ensuring isolated and consistent results.
- **Recovery**: Facilitates database recovery and error handling, ensuring committed transactions persist while incomplete ones do not affect the database state.

By adhering to ACID properties, database systems can ensure that transactions are processed reliably, providing a robust environment for data management and processing.
