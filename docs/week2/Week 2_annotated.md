# Week 2_annotated.pdf (PDF file)

**Summary**
**Information Representation**

Computers operate solely on "bits," which are binary digits with values of 0 or 1. Numbers can be represented using bit patterns, such as 6 being represented as 0110 in binary. Negative numbers can be represented using the two's complement notation, such as -6 being represented as 1010.

Textual information presents a challenge as it consists of arbitrary characters. ASCII is a 7-bit encoding standard that defines codes for common characters such as letters, numbers, and special symbols. However, ASCII is limited to 128 different entities, making it insufficient for representing text in many languages that use non-Latin characters.

**Unicode and UTF-8**

Unicode is a character encoding standard that aims to provide codes for all living and historical languages. It uses UCS (Universal Character Set) encodings, such as UCS-2 (2 bytes per character) and UCS-4 (4 bytes per character), to accommodate a vast number of characters.

UTF-8 is a variable-length encoding format for Unicode that uses 8-bit units. It is widely used on the web because it is efficient for representing common characters while also supporting a wide range of languages.

**Markup vs Style**

Markup languages like HTML focus on separating content from its presentation. HTML tags provide semantic meaning to the content, such as indicating a heading (<h1>) or a paragraph (<p>). On the other hand, style sheets like CSS are used to specify the visual presentation of the content, such as font size, color, and layout.

**HTML (HyperText Markup Language)**

HTML is the predominant markup language for the web. It allows content to be structured using tags, which can be nested to create complex documents. HTML5 introduced new tags and features, such as <header>, <nav>, and <footer>, to enhance the semantic representation of content.

**Document Object Model (DOM)**

The DOM is a tree-like representation of an HTML document that allows developers to programmatically manipulate the content and structure of the document. Using the DOM, developers can add, remove, or modify elements and their attributes.

**CSS (Cascading Style Sheets)**

CSS is used to control the presentation of an HTML document. It allows developers to specify the visual appearance of different elements, such as font, color, size, and layout. CSS can be applied inline (within HTML elements), internally (within the <head> tag), or externally (in a separate style sheet).

**Responsive Design**

Responsive design is an approach to web design that ensures the website adapts to different screen sizes and form factors, such as desktops, laptops, tablets, and smartphones. By using CSS media queries, developers can define different styles for different screen sizes, ensuring optimal user experience on all devices.

**Bootstrap**

Bootstrap is a popular CSS framework that provides pre-built styles and components for common web elements, such as buttons, forms, and navigation bars. It simplifies the development of responsive web designs by offering a consistent and mobile-first approach.

**JavaScript**

JavaScript is a scripting language that is integrated into the web browser. It allows developers to add interactivity and dynamic behavior to web pages, such as handling user input, manipulating the DOM, and creating animations. JavaScript is essential for enhancing the user experience on the web.
