To check if a string is a valid JSON format by looking at it, you can follow these guidelines:

1. **Braces and Brackets**:

   - JSON objects are enclosed in curly braces `{}`.
   - JSON arrays are enclosed in square brackets `[]`.
2. **Key-Value Pairs**:

   - JSON objects contain key-value pairs.
   - Keys must be strings enclosed in double quotes `"`.
   - Values can be strings (in double quotes), numbers, objects, arrays, `true`, `false`, or `null`.
3. **Commas**:

   - Key-value pairs within an object are separated by commas.
   - Elements within an array are separated by commas.
4. **Colons**:

   - A colon `:` separates keys from values in an object.
5. **Strings**:

   - Strings must be enclosed in double quotes `"`.
   - Single quotes `'` are not allowed for strings.
6. **Whitespace**:

   - Whitespace is allowed and ignored around or between syntactic elements (e.g., spaces, tabs, newlines).

### Example of Valid JSON

```json
{
    "name": "John",
    "age": 30,
    "isStudent": false,
    "courses": ["Math", "Science"],
    "address": {
        "street": "123 Main St",
        "city": "Anytown"
    }
}
```

### Example of Invalid JSON

```json
{
    name: "John",  // Keys must be in double quotes
    "age": 30,
    "isStudent": false,
    "courses": ["Math", "Science"],
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
    }  // Trailing comma is not allowed
}
```

### Common Mistakes to Look For

1. **Missing Quotes**: Keys and string values must be in double quotes.

   ```json
   {name: "John"}  // Invalid
   {"name": "John"}  // Valid
   ```
2. **Trailing Commas**: No trailing commas are allowed after the last item in objects or arrays.

   ```json
   {"name": "John",}  // Invalid
   {"name": "John"}  // Valid
   ```
3. **Incorrect Braces/Brackets**: Ensure all opening braces `{` and brackets `[` have corresponding closing braces `}` and brackets `]`.

   ```json
   {"name": "John"  // Invalid
   {"name": "John"}  // Valid
   ```
4. **Use of Single Quotes**: JSON does not allow single quotes for strings.

   ```json
   {'name': 'John'}  // Invalid
   {"name": "John"}  // Valid
   ```

By following these guidelines, you can visually inspect a JSON string to determine if it is likely valid.
