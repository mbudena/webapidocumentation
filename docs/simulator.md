# API Environments, and the API simulator

Before access to the production API Gateway is provided, testing of API consumer code needs to complete, and be signed off. In order to facilitate development and testing, non-production environments are made available.

The API environments are as follows:

- API Simulator
- End to End (ETE) Environment
- Production Environment

These environments differ, as detailed in the following sections.

## API Simulator

The API simulator is an instance of the API gateway deployed to a non-production environment, using stubbed internal integration instead of connecting to the various Telco internal systems that the ETE and Production environments do.

This environment uses a pre-built profile, shared by all users of the environment.

Validation of some attributes in the API payloads does not take place, as it would on any other environment. Specifically, ICCIDs Deal ID, and MSISDNs are not validated.

This allows development testing to proceed without the configuration of per API consumer profiles,
Deal Sheets, MSISDNs, and SIM inventories.

Responses from Telco internal systems are typical of production, and the same results returned for all requests for any specific API operation. For example, in the case of a successful POST Order API operation, the same Order ID and MSISDN will always be returned.

Validation of API request json payloads are therefore validated only for specific aspects, such as:

- Correct http headers
- Correct Authentication (using a shared credential)
- Correct json payload structure

Simulation of specific failure modes is accommodated, by the inclusion of a http header.

This allow for unit testing of API consumer code.

Once an API consumer's code is able to successfully call all the API operations in scope, the API consumer can sign-off on unit testing, and proceed to End to End testing.

## End to End environment (ETE)

Use of an ETE is governed by the IT Change Request (CR) process, and is scheduled into a Quarterly Release.

To enable use of the ETE environment, some internal preparation is required, that is managed as part of the CR process.

Internal preparation includes the following activities, which mimics the production environment:

- Creation of records in the Telco OSS/BSS systems for the API consumer Customer
- Creation of a profile with authentication and authorisation detail matching the BSS/OSS system
- Creation of test data for use on the ETE environment, such as MSISDNs and ICCIDs
- Determination of Deals IDs valid on the ETE environment

Once the preparation is complete API calls can be made by the API consumer, which trigger ordering and service configuration operations in Telco internal OSS/BSS systems of the ETE environment, and API responses provide production realistic values, including validation failures.

API requests therefore need to make use of valid values in the URL and payload, such as Deal IDs, ICCIDs, Order IDs and MSISDNs.

Values returned from API operations represent responses and statuses that the API Gateway receives from Telco internal OSS/BSS systems in the ETE environment.

## Production Environment

Similar to the ETE environment, there is preparation required on the Production environment.

In this case, ICCIDs represent physical SIMs, and the Deal IDs would correspond to Deals found in the Deal Sheet provided by the Telco Account Manager. MSISDNs used in API operations would need to represent actual mobile services.
