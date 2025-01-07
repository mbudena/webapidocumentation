# Error Codes

Error information returned from failed API calls always include standard HTTP response codes.

In addition, for some error scenarios, a json response payload with further error information is returned.

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

- Error Code
- Error Reason
- Error Message
- Status

As example error response payload:

```json
{
  "code": "APN-PO-0002:GetCustomerDetails:1:WS-PO-0001",
  "reason": "Authorization error",
  "message": "Authorization Failed: Corporate Customer is not allowed to perform this service",
  "status": "401:APN-PO-0002"
}
```

In instances where the processing failure in a downstream system, error responses from the downstream system
are encoded into the response payload.

## Structure of the Error Body Response

| Element | Structure or description                                                              |
|---------|---------------------------------------------------------------------------------------|
| Code    | API_GW_ERROR_CODE:ESB_WRAPPER_NAME:ESB_RESULT_CODE:ESB_MESSAGE_CODE                   |
| Reason  | API_GW_ERROR_EXPLANATION                                                              |
| Message | ESB_RESULT_MESSAGE                                                                    |
| Status  | HTTP_CODE:API_GW_ERROR_CODE                                                           |

### Description of encoded information in the error response json

| Parameter                | Description                                                         |
|--------------------------|---------------------------------------------------------------------|
| API_GW_ERROR_CODE        | API Gateway error code                                              |
| ESB_WRAPPER_NAME         | Downstream API operation                                            |
| ESB_RESULT_CODE          | Downstream API result code                                          |
| ESB_MESSAGE_CODE         | Downstream message code                                             |
| API_GW_ERROR_EXPLANATION | Technical supporting information related to the error               |
| ESB_RESULT_MESSAGE       | Downstream API result message                                       |
| HTTP_CODE                | HTTP response code                                                  |
