
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
    - Databases would be used
    - Front end would be reactive (Vue, React, etc.)
    - API would be blueprinted and standardized 
    - Scroll indication overlay on log card bodies
    - Actual folder structures for the code

- In the current system, two clients could request and get logs from slightly different times than expected, but the logs are timestamped internally, so shouldn't cause any issues.


### References

- Spinner CSS
    - https://tobiasahlin.com/spinkit/
- JQuery
    - 
- Bootstrap
    -