
- **PostgreSQL Startup, Schema Setup, and Node.js Connection Test**

```shell
# Pull the latest PostgreSQL image from Docker Hub
docker pull postgres:latest
```

```shell
# Run the PostgreSQL container with these settings:
# - Container name: my-postgres
# - Set the postgres superuser password to "mysecretpassword"
# - Run in detached mode with local port 5432 mapped to container port 5432
docker run --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 postgres:latest
```

```shell
# Check container logs to verify startup
docker logs my-postgres
```

- output

```shell
[2025-02-27T12:34:56Z] INFO: Starting container "my-secure-app"...
[2025-02-27T12:34:56Z] INFO: Initializing TLS configuration...
[2025-02-27T12:34:56Z] ERROR: TLS initialization failed: no valid root CA certificate found.
[2025-02-27T12:34:56Z] ERROR: x509: certificate signed by unknown authority.
[2025-02-27T12:34:57Z] WARN: Retrying TLS handshake (attempt 1 of 3)...
[2025-02-27T12:34:57Z] ERROR: TLS handshake failed: x509: certificate signed by unknown authority.
[2025-02-27T12:34:58Z] ERROR: Container shutdown initiated due to fatal TLS configuration error.
```

> **Note:** If the logs show errors such as "FATAL: password authentication failed for user 'postgres'", review your environment settings and container configuration.

---

- **Creating an Application User and Schema**

```shell
# Connect to PostgreSQL using psql
psql -h localhost -U postgres -d postgres
```

```shell
# Inside the psql shell, execute the following SQL commands:
CREATE USER appuser WITH PASSWORD 'appsecret';
CREATE SCHEMA appschema AUTHORIZATION appuser;
```

> **Notes:**  
> This creates a new user (`appuser`) with its password and an associated schema (`appschema`) for your application.  
> Ensure that your Node.js service uses these credentials when connecting to PostgreSQL.

---

- **Node.js Connection Issue**


```shell
# In your Node.js service, connection settings are typically loaded from environment variables.
# .env file contain:
#   DB_USER=appuser
#   DB_PASSWORD=<REDACTED BAD PASSWORD ENDING IN H#>
#   DB_HOST=localhost
#   DB_PORT=5432
#   DB_DATABASE=postgres-mail-list-users-v1
#
# Attempting to connect with these incorrect credentials may yield an error like:
FATAL: password authentication failed for user "appuser"
```
> Looks like I pulled the wrong password from vault

- Output when we where missing tls cert

```shell
[2025-02-27T14:23:10.001Z] INFO: Starting Node.js backend service...
[2025-02-27T14:23:11.004Z] INFO: Attempting to connect to PostgreSQL at postgres://localhost:5432/mydb
[2025-02-27T14:23:11.005Z] ERROR: Failed to establish a secure connection to PostgreSQL.
[2025-02-27T14:23:11.006Z] ERROR: Connection error: self-signed certificate in certificate chain (Error: UNABLE_TO_VERIFY_LEAF_SIGNATURE)
[2025-02-27T14:23:11.007Z] WARN: Check your environment variables for DB credentials and TLS settings.
[2025-02-27T14:23:11.008Z] INFO: Retrying connection in 5000ms...
```

> **I wonder if** the issue stems from a misconfiguration in your environment variables—double-check that the `DB_PASSWORD` matches the password set during the schema creation (i.e., "appsecret").

