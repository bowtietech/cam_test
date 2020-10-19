
### Overview

This server is written to handle multiple cameras and clients simultaneously.

### Prerequisites

- A computer
- Git
- Docker
- Docker Compose

### Installation and Running

***Important*** Make sure that port 3000 is not already in use.

In the project root directory, run the command:
```
docker-compose up -d
```

This will run the program as a daemon, and build automatically if necessary.




### Stopping

In the project root directory, run the command:
```
docker-compose down
```

### Considerations & Deviations From Instructions

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
    - There would be a POST route explicit for logs instead of root
    - Would use ENV variables instead of hardcoding

- In the current system, two clients could request and get logs from slightly different times than expected, but the logs are timestamped internally, so shouldn't cause any issues.
- ***IMPORTANT*** The user's '/logs' request will complete with whatever data is available, but invalidated if not current (contrary to instructions). Leaving the GET request open that long seemed dirty, dirty. 

### References

- Spinner CSS
    - https://tobiasahlin.com/spinkit/
- JQuery
    - https://jquery.com/
- Bootstrap
    - https://getbootstrap.com/