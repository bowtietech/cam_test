
### Overview

This server is written to handle multiple cameras and clients simultaneously.

### Installation


### Running



### Considerations

- In a production system, we would:
    - Use authentication with MFA of some kind, likely SSO (Okta, etc.)
    - Logs would be stored outside RAM and paginated
    - It wouldn't be so hastily put together
    - Unit and API tests would be included
    - Error checking on all values
    - Serve a favicon
    - Concatenate logs on the server to keep the cam's memory free
    - Add a registration route for new cameras
    - Would document with numpydoc style or equivalent for doc generation and readability
