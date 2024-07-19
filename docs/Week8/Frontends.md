# Frontends

**Summary**

## Frontends

### Definition and Components

A frontend in the context of application development refers to the user-facing interface, which interacts with the user directly. The frontend is responsible for presenting information, receiving input, and facilitating user interaction.

Key components of a frontend include:

- **Device/OS Specific Controls and Interfaces:** Tailored to the specific hardware and operating system of the device being used.
- **Web Browser Standardization:** Common conventions adopted by multiple browsers to ensure consistent rendering and functionality.
- **Browser vs. Native:** Different approaches to frontend development, with browsers offering cross-platform compatibility and native applications providing optimized performance.

### Web Applications and Frontend Mechanisms

Web applications are frontend applications that run within a web browser. They typically leverage a combination of HTML (Hypertext Markup Language), CSS (Cascading Style Sheets), and JavaScript to define the user interface, style, and behavior.

Frontend mechanisms in web applications involve:

- **HTML:** Defines the content and structure of the web page.
- **CSS:** Controls the presentation and styling of the elements within the web page.
- **JavaScript:** Enables dynamic interactions, such as form validation, event handling, and asynchronous data retrieval.

### Types of Frontend Generation

**Fully Static Pages:**

- All or most pages on a website are pre-generated and stored as static files.
- Offers high performance as the server simply delivers cached files.
- Limited ability to adapt to runtime conditions, such as user login or time-of-day.

**Run-time HTML Generation:**

- HTML is dynamically generated on the server side each time a page is requested.
- Provides greater flexibility for adapting to runtime conditions and incorporating database interactions.
- Introduces server load implications and performance bottlenecks.

### Client-Side Scripting and Computation

**Client-side Scripting:**

- JavaScript is executed on the client (user's device) rather than the server.
- Enables more dynamic and engaging interactions, such as form validation, animations, and real-time updates.

**Client-side Computation:**

- Moving computational tasks from the server to the client can improve performance and reduce server load.
- Can be achieved through JavaScript or dedicated frameworks, such as WebAssembly.

### Security Implications

**Client-side Security Vulnerabilities:**

- JavaScript code running on the client can potentially be exploited to access sensitive data or manipulate the user interface.
- Cross-site scripting (XSS) attacks are a common concern.

**Server-side Security Vulnerabilities:**

- Dynamically generated HTML on the server can be susceptible to injection attacks (e.g., SQL injection, command injection).
- Proper input validation and escaping mechanisms are crucial.

### Tradeoffs and Considerations

**Server-side Rendering:**

- Flexible and easy to develop
- May introduce performance bottlenecks on dynamic pages
- Potential for security issues on the server

**Fully Static Pages:**

- Excellent performance
- Limited interactivity and adaptability
- Requires re-compilation for changes

**Client-side Rendering:**

- Reduces server load
- Enables more dynamic interactions
- Raises potential security concerns on the client
- Requires additional resources on the client device

### Estimating Performance

Performance benchmarks for web servers indicate:

- Static pages: Apache ~10,000 requests/second, Nginx ~20,000 requests/second
- Dynamic pages: Both ~100 requests/second (limited by PHP rendering)
- Dynamic pages occupy more server resources and are harder to scale efficiently
