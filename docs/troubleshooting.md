# Troubleshooting

The tables below provide further information on typically encountered errors, with suggested actions. This is followed by investigation and troubleshooting advice.

## Validation Errors

| HTTP | ERROR CODE   | ERROR MESSAGE | ACTION |
|------|--------------|---------------|--------|
| 400  | CONS-PO-0003 | This service ID currently has open orders, your order cannot be processed | Investigate and resolve open order on the service |
| 400  | CONS-PO-0004 | Subscriber details for this MSISDN were not found. | Investigate and resolve service state |
| 500  | CONS-PO 0005 | This SIM number {ICCID} has already being used | Investigate SIM status |
| 500  | ESB-1        | Business Error Customer information: Not retrieved. | Please report to the support team. |

## Deal related errors

| HTTP | ERROR CODE   | ERROR MESSAGE | ACTION |
|------|--------------|---------------|--------|
| 400  | Cons-po-0002 | Requested completion date cannot be before today’s date. | Adjust the Requested completion date to one in the future. |
| 500  | WSE-500      | Agent ID with {id} does not exist in CRM database | Please report to the support team. |
| 500  | WSE-500      | The deal ID is not recognised. Must be one of (valid deal IDs) | Investigate Deal ID |
| 500  | WSE-500      | The deal name is not recognised. Must be one of (valid deal names) | Investigate Deal name |

## Cache errors

| HTTP | ERROR CODE   | ERROR MESSAGE | ACTION |
|------|--------------|---------------|--------|
| 500  | WSE-500      | Web Service Business Error LPDH – Object not found for requested ID. | Retry after an hour. |
| 500  | LPDH_ GOE06  | Web Service Error BAN or Offer could not be found for ServiceID | Please retry later. If consistent, could be a symptom of an earlier order failing, or a ceased service. |
| 500  | WSE-501      | Web Service Technical Error LPDH_GCRS02: Service ID not Found in CRM, OMS or Huawei | Please retry later. |

## Communication errors

| HTTP | ERROR CODE   | ERROR MESSAGE | ACTION |
|------|--------------|---------------|--------|
| 550  | WSE-501      | PortalWSSOAPClientExcepion: Internal Server Error | Please report to the support team. |
| 500  | WSE-501      | PortalWSSOAPClientException: I/O error: Read timed out; | Please report to the support team. |
| 500  | GATE-0004    | Connectivity Error occurred during the service invocation | Please report to the support team. |
| 500  | GATE-0004    | Technical Error Timeout occurred during the service invocation | Please report to the support team. |

## Troubleshooting Orders

### Requested completion date

- Requested completion date needs to be in the future. For orders requiring immediate provisioning, a time a few minutes in the future will allow for latency before date validation.
- The requested completion date needs to be within the next six months.

### Deal IDs and Deal Names

- Deal reference information is provided in the form of a *Deal Sheet* from the Account Manager.
- **NOTE**: The string " Deal" should be appended to the deal names typically provided in the deal sheet.

### Tracking Order progress

- Order status queries sooner than 15 minutes of acceptance may fail due to cache latency.
- For asynchronous orders, the GET */cons-po/ProductOrder/v1/productOrder/{id}* operation should be used
- Orders with a status of **Negotiation** are being processed.
- Orders with a status of **Done** are complete.
- Orders with a status of **Delivery** are waiting tor the future date specified, for provisioning.
- Orders in status **Negotiation** after an hour of placement should be reported to the support team.
- Recommended order completion polling: Query every 15 minutes till Done or Delivery, or an hour as passed.

### Errors Querying Orders

- Use the productOrderGet API */cons-po/ProductOrder/v1/productOrder/{id}* to get the status of the order.
- *WSE-500* typically indicates that asynchronous order is not yet processed, and the result not available in the LPDH cache. Retry in an hour.
- *LPDH_GOE06* Could be a symptom of an earlier order failing, or a ceased service.

## Investigating Services

- The */cons-ac/Activation-Config/v1/service/{id}* API operation should be used to query service state.
- The MSISDN provided on order acceptance will not reflect in caches as active immediately, and may take up to an hour to reflect in caches used for queries.

## Investigating SIM issues

- *CONS-PO 0005* The SIM is already active on the network. Investigate SIM status. If you have reason to believe that a false positive on the verification, please report this to the API support team.

- On an end to end verification environment: Retry with a known unused ICCID from the supplied test data. Request additional end to end test ICCIDs from the Onboarding Support team if required.

## Reporting Issues

Please provide the full request and response when reporting an issue, to assist with a quick resolution.
