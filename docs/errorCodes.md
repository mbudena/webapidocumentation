# Error Codes

Error information returned from failed API calls always include standard HTTP response codes.

Web APIs expect HTTP POST or GET request to application. A response will then be returned in the form of a JSON response.


## HTTP Response codes

The HTTP response codes are included in the response header. 

2XX series responses indicate success.

4XX series responses indicate an API client error.

5XX response error codes indicate a server error. Server errors include client request attribute or business rule failure scenarios,
such as downstream validation failures.

| Code | Description                                                                                                                       |
|------|-----------------------------------------------------------------------------------------------------------------------------------|
| 201  | OK: Used to indicate HTTP GET success.                                                                                            |
| 201  | Created: Used to indicate successful resource creation in synchronous processes.                                                  |
| 202  | Accepted: Used to indicate successful acceptance or requests in asynchronous processes.                                           |
| 400  | Bad Request: This is used to indicate a non-specific failure, indicating that the request could not be understood by the server.  |
| 401  | Unauthorized: This is returned when the request did not include valid credentials.                                                |
| 403  | Forbidden: The user is not authorised for the operation, or resource. An error payload may be returned, providing further detail. |
| 410  | Bad Format: Either the request structure is invalid, or there are missing mandatory attributes.                                   |
| 500  | Internal Server Error: Indicates downstream technical and business rule failures. An error payload is also returned.              |

## API Response Error Payload

In cases where further information on the cause of an error is provided, it is in the form of a json response body with the following elements:

- resultCode

One of the return parameters returning a value with the following standards.

| Vaule | Description |
|-------|----------|
|0      | No error has occurred.  |
|1      | An error/exception has occurred. Error codes larger than zero usually depict a business-related error.   |
|-1     | An error/exception has occurred. Error codes less than 0 imply a technical error has occurred.   |

- resultMessageCode

 The resultMessage is not intended for customers. It provides the developer or support with more information around the reponse.

- friendlyCustomerMessage

 Reference code used by the APIs to help us with identifying problems on our side. These should map to a result code in this document

- payload

 The payload contains all the information which can be consumed by the view layer. Information is packaged up and put into the payload. In the case where an error has occurred, the payload will always be empty. Payload could be empty for successful transactions too.

As example error response payload:

```json


    "resultCode": 1,
    "resultMessageCode": "api-bus-004",
    "resultMessage": "Could not retrieve billing usages history summary.",
    "friendlyCustomerMessage": "",
    "payload": {}


```

In instances where the processing failure in a downstream system, error responses from the downstream system are encoded into the response payload.
