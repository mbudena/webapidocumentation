
# Authentication and Authorization

Access to the web APIs requires authentication. The supported authentication method is:

- **OAuth 2.0 Bearer Token**

Usernames and passwords are sourced from the Telkom Portal Identity and Access Management (IAM) system. This integration allows users to manage password changes and resets via the Telkom Web GUI, consistent with applications like Telkom Consumer Self Service and the Enterprise Self Service Portal (ESSP).

> **Note:** If a user changes their password through the Telkom Web GUI, the API web client implementation must be updated accordingly.

---

## Authentication Process

To authenticate, follow these steps:

### 1. Obtain Telkom Portal Credentials

Ensure you have a registered **username** and **password** on the Telkom Portal.

### 2. Profile Construction

The API Gateway Support team will create a profile linking your credentials to the appropriate Telkom CRM Customer:

- **Phase III** – Onboarding for End-to-End verification environment.
- **Phase IV** – Onboarding for Production environment.
- **Phase II** – Simulator environment (shared credential).

> ⚠️ Ensure neither the `username` nor `password` contains control characters or the colon (`:`), which is used as a separator in the BAA scheme.

---

## Steps to Authenticate

### Step 1: Register Client Handle

**Request:**

```http
POST <production-server>/oic_rest/rest/mobileoamauthentication/register
X-IDAAS-SERVICEDOMAIN: MobileServiceDomain
Content-Type: application/json
```

**Body:**

```json
{
  "X-Idaas-Rest-Subject-Type": "USERCREDENTIAL",
  "X-Idaas-Rest-Subject-Username": "your_username",
  "X-Idaas-Rest-Subject-Password": "your_password",
  "X-Idaas-Rest-New-Token-Type-To-Create": "CLIENTREGHANDLE",
  "deviceProfile": {
    "oracle:idm:claims:client:sdkversion": "",
    "oracle:idm:claims:client:ostype": "",
    "oracle:idm:claims:client:osversion": "",
    "hardwareIds": {}
  },
  "clientId": "Telkom"
}
```

---

### Step 2: Receive Client-Secret Token

**Response:**

```json
{
  "X-Idaas-Rest-Token-Type": "CLIENTREGHANDLE",
  "X-Idaas-Rest-Token-Value": "eyJvcmFjbGU6aWRtOm.."
}
```

---

### Step 3: Generate a User Token

1. Prepend the token with `Telkom:`  
2. Base64 encode the result  
3. Use it in the `X-Idaas-Rest-Authorization` header

**Example:**

- Original token: `eyJvcmFjbGU6aWRtOm..`
- Concatenate: `Telkom:eyJvcmFjbGU6aWRtOm..`
- Base64 encode: `Base64("Telkom:eyJvcmFjbGU6aWRtOm..")`

**Use in header:**

```http
X-IDAAS-SERVICEDOMAIN: MobileServiceDomain
X-Idaas-Rest-Authorization: UIDPASSWORD cred="<Base64_encoded_string>"
Content-Type:application/json
```

**Body:**

```json
{
  "X-Idaas-Rest-Subject-Type": "USERCREDENTIAL",
  "X-Idaas-Rest-Subject-Username": "your_username",
  "X-Idaas-Rest-Subject-Password": "your_password",
  "X-Idaas-Rest-New-Token-Type-To-Create": "USERTOKEN",
  "deviceProfile": {
    "oracle:idm:claims:client:sdkversion": "",
    "oracle:idm:claims:client:ostype": "",
    "oracle:idm:claims:client:osversion": "",
    "hardwareIds": {}
  },
  "clientId": "Telkom"
}
```


**Response:**

```json
{
  "X-Idaas-Rest-Provider-Type": "OAM_11G",
  "X-Idaas-Rest-Token-Type": "USERTOKEN",
  "X-Idaas-Rest-Token-Value": "j0Y9XHqk+MX1z4B5f6r4a0D6JoYim6p0...",
  "X-Idaas-Rest-User-Principal": "sanlam@test.com"
}
```

---

### Step 4: Generate Access Token

1. Make an unauthorized request to a protected API
2. Capture the `request-ctx` from the response headers
3. Use `request-ctx`  in request body and get access token

**Request headers:**

```http
X-IDAAS-SERVICEDOMAIN: MobileServiceDomain
Content-Type: application/json
User-Agent: OIC-Agent
```

**Response header example:**

```http
WWW-Authenticate: OAM-Auth realm="...", request-ctx="encquery%3DluHq%2BADwTADDCXsILpll5Hy%2FPQGwkYwQ..."
```

Use this `request-ctx` in your next token generation step.

**Generate access token**

```http
X-IDAAS-SERVICEDOMAIN: MobileServiceDomain
X-Idaas-Rest-Authorization: UIDPASSWORD cred="<Base64_encoded_string>"
Content-Type:application/json
```

**Body:**
```json
{
  "X-Idaas-Rest-Subject-Type":"TOKEN",
  "X-Idaas-Rest-Subject-Value":"{{user_token}}",
  "X-Idaas-Rest-Application-Context":"encquery%3DluHq%2BADwTADDCXsILpll5Hy%2FPQGwkYwQ...",
  "X-Idaas-Rest-Application-Resource":"https://ecdev02selfservice.telkom.co.za/onnet/protected/api/getFreeResources",
  "X-Idaas-Rest-New-Token-Type-To-Create":"ACCESSTOKEN"
}
```

**Response**

```json
{ 
"X-Idaas-Rest-Provider-Type":"OAM_11G",
"X-Idaas-Rest-Token-Type":"ACCESSTOKEN",
"X-Idaas-Rest-Token-Value":"qMn46VUXCL39py%2FV1ByL%2BaTyDF8wIgxkJC6ZEV ...",
"X-Idaas-Rest-User-Principal":"sanlam@test.com"
}
```


## Step 5: Access Protected Resources

Use the access token in the Authorization header to access protected endpoints.

### Example Request:

```http
GET https://.../getAccountFinancialSummary
Content-Type: application/json
User-Agent: OIC-Agent
Authorization: OAM-Auth {{access_token}}
```


### Response:

```json
{
  "resultCode": 0,
  "resultMessageCode": "api-afc-000",
  "resultMessage": "",
  "friendlyCustomerMessage": "",
  "payload": { ... }
}
```
