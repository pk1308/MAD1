### REST (REpresentational State Transfer)

- REST is a software architecture style for distributed systems on the web.
- REST defines a set of constraints that guide the design of web services.
- REST is based on the idea of representing state in the form of resources that are transferred between clients and servers.

### REST Sequence

- **Client accesses a Resource Identifier from server:** Typically a URI (Uniform Resource Identifier).
- **Resource Operation specified as part of access:** E.g., GET, POST, PUT, DELETE.
- **Server responds with new Resource Identifier:** New state of system and links to follow.

### Using HTTP with REST

- HTTP (Hypertext Transfer Protocol) is a protocol that can be used to carry REST messages.
- HTTP verbs (e.g., GET, POST, PUT, DELETE) are used to indicate actions.
- HTTP provides standardized functionality.

### Using JSON with REST

- JSON (JavaScript Object Notation) is a data format that is commonly used with REST APIs.
- JSON is a lightweight and easy-to-read format that can represent complex data structures.

### API Data Transfer Format

- **Input to API:** Text (e.g., HTTP)
- **Output:** Complex data types (e.g., JSON, XML)
- **Different from internal server representation**
- **Different from final view presentation**


**Examples of REST APIs**

* Wikipedia: Search for pages, view page history, and retrieve JSON output
* CoWin: Book vaccine appointments, search for vaccination centers
* Twitter: Post tweets, view timelines, and follow users

**Typical Functionality**

REST APIs typically offer a range of functionalities, including:

* **CRUD operations (Create, Read, Update, Delete)**
* **Listing (querying and filtering data)**
* **Specialized functions (e.g., creating virtual machines, rebooting servers)**

**Formal Specifications**

Formal specifications, such as OpenAPI, help developers understand and use REST APIs effectively. They define the endpoint URLs, request and response formats, and error codes.

**Authentication**

Many APIs require authentication to protect user data and prevent abuse. Common authentication methods include:

* **Tokens:** Unique identifiers issued to valid users
* **API Keys:** One-time tokens that can be downloaded by users

**Benefits of REST APIs**

* **Interoperability:** Allows seamless integration with third-party applications
* **Simplified development:** Provides a clear and concise design framework
* **Scalability:** Supports high volumes of requests without compromising performance

**Detailed Documentation**

Comprehensive documentation is essential for understanding the capabilities of a REST API. It includes:

* **Endpoint URLs and parameters**
* **Request and response formats**
* **Error codes and handling**

**Testing REST APIs**

To ensure proper functioning, REST APIs should be thoroughly tested. This can be done using tools like curl or Postman. However, excessive testing should be avoided to prevent overloading servers.

**Summary**

REST APIs are powerful tools for creating web services that can be accessed and integrated by various applications. They offer a wide range of functionalities, including CRUD operations, listing, and specialized functions. Authentication mechanisms ensure data protection and prevent abuse. Formal specifications provide guidance for developers, and detailed documentation simplifies API implementation. By leveraging REST APIs, developers can create interoperable, scalable, and user-friendly systems.
