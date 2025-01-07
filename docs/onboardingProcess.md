# Onboarding Process

## Onboarding Phases

For clarity, the onboarding of API consumers is split into four phases:

- Phase I: Documentation
- Phase II: Coding and Unit testing
- Phase III: End to End testing
- Phase IV: Production implementation

### Phase I: Documentation

The documentation phase precedes the provision of access to API platforms.

The following activities are relevant to this phase:

- Commercial Agreements: The singing of Business contracts and agreements.
- Network Access Agreements: The singing of Network access agreements.
- Scope Determination: Documenting which operations will be used by the API consumer, which in turn determines the scope items for the Telco internal IT Change Request process, and therefore also the test result schedules.
- API documentation: Provision of access to API technical documentation.
- IT Change Request initiation: Preparation of the formal inputs to the IT Change Request (CR) process.

### Phase II: Coding and Unit testing

Once the documentation is in place, access to a sandbox environment, that simulates the APIs in scope, is granted. The intention of this phase is to allow the consumer to exercise the API, observe typical behaviour, and unit test code, without an assigned ETE environment.

The following activities are relevant to this phase:

- Technical start-up meeting: The API support team, and the API consumer technical team meet to provide a high level description of API usage, and demonstrate of the use of the sandbox.
- Sandbox Access: Granting of access to a simulator environment for the API operations in scope.
- API Consumer coding: The writing of software by the API consumer technical team.
- API development support: The API Support team is available for scheduled sessions to answer questions, provide guidance, and assist with troubleshooting.
- API Consumer unit testing: The testing of API consumer code, using the API sandbox
- Completion acceptance: Acceptance of API consumer code for the API operations in scope.
- End to End test scheduling: The assignment of the API Consumer Onboarding CR to a Scheduled Release. There are four CR Scheduled Releases in a year, and end to end testing for the API Consumer needs to be assigned to one of these.

### Phase III: End to End testing

Once the CR scheduled release window opens, an end to end (ETE) testing environment is assigned, and the complete end to end process for API operations in scope can be validated.

The following activities are relevant to this phase:

- Assignment of CR Project Manager: An IT project manager (PM) is assigned to the CR, to drive delivery.
- Assignment of ETE environment: The IT PM negotiates for a telco internal platform, with integrated back-end systems, to the Onboarding CR, for the duration of the scheduled release.
- Preparation of ETE environments: The teams responsible for the various integrated back-end environments deploy production versions of software to their ETE environment integrated platforms, and complete readiness testing (Business Unit Availability Testing).
- Creation of Test Data: The data entities in the integrated back ends necessary for end to end testing of the API operations in scope are created by the SQA team.
- Creation of API Consumer Gateway Profile: The profile linked to API Authentication and Authorisation is created on the ETE environment, and API endpoint and access details shared with the API consumer.
- Sharing of ETE testing data with the API consumer: Details of created and consumable resources, and reference data for the ENT testing is shared with the API Consumer technical team
- Conducting of End to End testing: API Consumer code for each operation in scope is tested against the End to End environment.
- ETE Troubleshooting: The API Support team is available for scheduled sessions to answer questions, provide guidance, and assist with troubleshooting of testing failures.
- Completion acceptance: Acceptance of API consumer code for the API operations in scope, based on successful End to End testing for each API operation.

### Phase IV: Production implementation

Once successful end to end testing has been signed off, a production release date is scheduled.

Pre-requisites:

- SIM inventory: The API consumer (if making use of the CreateDeal or SIM swap operations), need to have mobile SIMs in stock.
- Deal metadata: The API consumer (if making use of the CreateDeal or Migrate operations), will need to use valid Deals, which are provided by their Account Manager, in the form of a Deal Sheet.

The following activities are relevant to this phase:

- Creation of Production API Consumer Gateway Profile: The profile linked to API Authentication and Authorisation is created on the production environment, and API endpoint and access details shared with the API consumer.
- The API consumer can now proceed with API transactions on the production system.
- Production Support: The first line API support team can be contacted using the API support process, and Production Incidents will be logged on behalf of the API consumer, if further investigation is required.
