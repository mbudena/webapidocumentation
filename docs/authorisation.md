# Authentication and Authorization

Authentication is required to access the Gateway APIs.

Standard **Basic Access Authentication**, built into the HTTP protocol, is used.

Usernames and passwords are re-used from the Telkom Portal Identity and Access Management (IAM) system.

This allows for password changes and resets to be manage on the Telkom Web GUI, in the same way as used for applications such as Telkom Consumer Self Service and Enterprise Self Service Portal (ESSP).

NOTE: If the password is changed by a Telkom Web GUI user in the normal course of use, the API Gateway client implementation must be adjusted accordingly.

## Basic Access Authentication

For convenience, the standard Basic Access Authentication (BAA) scheme defined in RFC 7617 is describe here, explained in the context of the Telkom Portal IAM platform.

The starting point is the username and password for a registered user on Telkom Portal.

For these to be usable by an API Gateway client, a profile needs to be constructed by the API Gateway Support team linking these credentials to the correct Telkom CRM Customer. This step occurs during the Phase III of the Onboarding process for the End to End verification environment, and during Phase IV for the Production environment. On the Simulator environment, in Phase II of the Onboarding process, a shared credential is used.

Note that for a credential to be usable on API Gateway, neither the username nor password should contain control characters, or the colon character (`:`) as this is used in the BAA scheme as a separator.

With the `username` and `password` described above, the *Authorization* HTTP header field is constructed and used in API Gateway HTTP requests as follows:

1. Create a string from the username and password separated by a colon (`:`).
2. Base64 encode the string created in step 1.
3. Prepend the Base64(username:password) string with the string `Basic ` (note the space).
4. This results in the string `Basic Base64(username:password)`
5. When constructing an API Gateway request, the `Basic Base64(username:password)` string is added as an HTTP header field with the header name `Authorization`.

### Example

1. Given a `username` *ExampleUsername*, and a `password` *ExamplePassword*, the string to be Base64 encoded is: *ExampleUsername:ExamplePassword*
2. `Base64(ExampleUsername:ExamplePassword)` equates to `RXhhbXBsZVVzZXJuYW1lOkV4YW1wbGVQYXNzd29yZA==`
3. `Basic Base64(username:password)` equates to `Basic RXhhbXBsZVVzZXJuYW1lOkV4YW1wbGVQYXNzd29yZA==`
4. As calculated above the `Authorization` header value is `Basic RXhhbXBsZVVzZXJuYW1lOkV4YW1wbGVQYXNzd29yZA==`
5. The required HTTP header line is therefore

```HTTP
Authorization: Basic RXhhbXBsZVVzZXJuYW1lOkV4YW1wbGVQYXNzd29yZA==
```

## References and Utilities

- Online Base64 encoder: <https://www.base64encode.org/>
- Basic Access Authentication RFP: <https://www.rfc-editor.org/rfc/pdfrfc/rfc7617.txt.pdf>