# CRUD

**Summary**
**CRUD Operations**

CRUD (Create-Read-Update-Delete) is a fundamental concept in database operations. It encompasses the essential operations performed on data:

**Create:**

* Adds a new entry to the database.
* Ensures that the entry does not already exist.
* Checks within the database to avoid conflicts.
* Considers mandatory and optional fields.

**Read:**

* Retrieves data from the database.
* Can involve summarizing data, such as counts, distributions, or histograms.

**Update:**

* Modifies existing data in the database.
* Can involve changing values, addresses, or dates.

**Delete:**

* Removes data from the database.
* Can be used to remove completed records or correct errors.

**API (Application Programming Interface)**

An API provides a standardized method for interacting with a server. It allows clients to access server functionality without knowing the underlying implementation. CRUD operations form a basic set of functionality for many APIs, particularly in the context of web applications.

**Controllers**

Controllers group related actions logically. Actions represent specific operations, while controllers organize those actions into meaningful categories. This separation allows for flexible and maintainable code.

**Separation of Concerns**

MVC (Model-View-Controller) is a design pattern that promotes the separation of concerns between different components of an application:

* **Models:** Represent the data and its behavior.
* **Views:** Display the data to users.
* **Controllers:** Process user input and interact with models.

This separation allows for flexibility and maintainability, as different components can be modified independently.

**Rules of Thumb**

* Views and controllers should be independent of the model.
* Controllers should not directly interact with databases.
* In practice, views and controllers often have close interdependencies.

**HTTP Verbs**

HTTP verbs convey different meanings in API interactions:

* GET: Retrieve data
* POST: Create new data
* PUT: Update existing data
* DELETE: Remove data

Understanding these concepts is crucial for designing and implementing efficient and user-friendly web applications.
