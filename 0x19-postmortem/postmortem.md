![Resolutional](./resolution.jpeg)


# Postmortem: Service Outage on AirBnB Clone Platform

---

## Issue Summary

Duration: 14:00 - 16:30 UTC (2 hours 30 minutes)

Impact: The AirBnB Clone platform was down, affecting 75% of users. Users were unable to access the main site, resulting in failed bookings and incomplete data retrieval from the database. The API endpoints on port 5001 were unresponsive, leading to a significant disruption in the service.
Root Cause: A configuration error in the Flask application server, particularly the port routing, led to the server being unreachable.

---

## Timeline

* 14:00 UTC: Issue detected by an ALX monitoring alert, which flagged multiple failed API requests.
* 14:05 UTC: The issue escalated to me, and I began investigating the application logs on port 5001.
* 14:15 UTC: Initial assumption was a database connection issue. I checked MySQL connections and database logs.
* 14:30 UTC: Further investigation led me to examine the Flask application configuration, specifically the server ports.
* 14:45 UTC: Misleading debugging path: I attempted to restart the MySQL database, assuming a corrupted data issue.
* 15:15 UTC: I discovered that the Flask server was configured to run on port 5000 instead of the intended port 5001.
* 15:30 UTC: I reconfigured the Flask application to use the correct port.
* 15:45 UTC: Service was restored and users were able to access the site and API endpoints.
* 16:30 UTC: All systems were confirmed stable, and monitoring was adjusted to prevent recurrence.

---

## Root Cause and Resolution

The root cause of the outage was a misconfiguration in the Flask application server setup. The development environment was set to run on port 5000 by default, but the production environment was intended to run on port 5001. This misalignment led to the server being unreachable on the expected port, causing the site and API endpoints to be unresponsive.

To resolve the issue, I reconfigured the Flask application to correctly bind to port 5001. This involved updating the Flask environment settings and restarting the application server. Once the correct port configuration was applied, the service was restored.

---

## Corrective and Preventative Measures

To prevent a recurrence of this issue, the following measures will be implemented:
1. Update Flask Configuration: Ensure that environment-specific configurations are clearly defined and correctly applied during deployment.
2. Enhanced Monitoring: Implement detailed port-specific monitoring to detect any misconfiguration early.
3. Automated Deployment Checks: Introduce automated checks in the deployment pipeline to verify the correct environment settings, including port configurations.
4. Training: Conduct a training session for the engineering team on the importance of environment-specific configurations and the potential impacts of misconfigurations.

---

## TODO

* Patch the Flask configuration files to enforce correct port settings across environments.
* Add monitoring on all production servers for port availability and responsiveness.
* Integrate automated configuration validation into the CI/CD pipeline.
* Schedule team training on environment management best practices.
* Revise and distribute updated environment configuration documentation.
