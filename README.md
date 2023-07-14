# Data Engineering Take Home: ETL off a SQS Queue

The main goal of this project is to build an ETL (Extract, Transform, Load) pipeline that will read JSON data from an AWS SQS Queue containing user login behaviour, mask fields that include personally identifiable information (PII), and publish the converted data to a PostgreSQL database.


# Project Setup

### Requirements

- Python 3.8+
- Docker
- Docker Compose
- pip
- AWS CLI (for local testing)


### Instructions to setup the project

1. Clone the github repository using this link
    https://github.com/pratikp676/etl-fetch-aws-sqs.git

2. Install the required Python packages using `pip`:
    ```
    pip install -r requirements.txt
    ```

3. Using Docker Compose, set up the local development environment: 
    ```
    docker-compose up -d
    ```

4. Check if the local access is working:

-   Use `awslocal` to read a message from the queue:
    ```
    awslocal sqs receive-message --queue-url http://localhost:4566/000000000000/login-queue
    ```

- Establish a connection to the PostgreSQL database and confirm that the table was created:
    ```
    psql -d postgres -U postgres -p 5432 -h localhost -W
    ```

Then, execute the following command:
    ```
    SELECT * FROM user_logins;
    ```


## Project Structure

The project is structured as follows:

- `app/`: The main application folder containing the source code for the ETL pipeline.
- `__init__.py`: Initializes the application package.
- `config.py`: Configuration file containing environment-specific settings.
- `main.py`: The main script responsible for executing the ETL pipeline.
- `mask_pii.py`: Module responsible for masking PII data.
- `postgres.py`: Module responsible for connecting to the PostgreSQL database and inserting records.
- `sqs.py`: Module responsible for reading messages from the SQS Queue.
- `utils.py`: Utility module which contains the hashing logic.
- `tests/`: Folder containing unit tests for the application modules.
- `docker-compose.yml`: Docker Compose configuration file to set up the local development environment.
- `requirements.txt`: File containing the required Python packages for the project.


## Running the ETL Pipeline: 

Run the following command from the project directory's root to launch the ETL pipeline:
```
python -m app.main
```
Using this command, records will be added to the PostgreSQL database by reading messages from the SQS Queue, processing them to extract and mask the appropriate data, and then inserting the entries.


## Running Unit Tests:

Execute the following command from the project directory's root to run the unit tests.
```
pytest tests/
```
The `tests/` folder's tests will all be run by this command, and the results will be shown.


## Assumptions: 

1. The JSON data in the SQS Queue has a uniform format and includes fields such as `user_id`, `device_type`, `ip`, `device_id`, `locale`, `app_version`, and `create_date`.
2. To maintain uniqueness while making sure the original data cannot be readily recovered, the PII data (IP and device_id) can be masked using a one-way hashing method (e.g., `SHA-256`).
3. The proper table schema for storing the processed records is configured in the PostgreSQL database.
4. The local development environment is configured by the given Docker Compose file, and local testing doesn't require any additional configuration.
5. Advanced features like scheduling or error handling are not included in the ETL pipeline because it is intended to be run as a standalone script.


## Next Steps: 

1. Increase the number of tries for reading from SQS and writing to PostgreSQL and add error handling.
2. To track the operation of the application and identify issues, use logging and monitoring.
3. To process fresh data on a regular basis, provide a scheduling mechanism or make the ETL pipeline accessible as a service.
4. Optimise data processing to increase performance, for as by processing messages in batches.
5. Incorporate end-to-end testing and integration testing into testing plan.


### Deployment in Production: 

We could utilise a managed container orchestration service, such as AWS Fargate or Kubernetes, to deploy this application in production; this would make it simple for us to manage, scale, and monitor the application in a real-world setting.


### Production-Ready Components:

We may incorporate the following elements to make this application production-ready:

1. Centralised logging for simple log management and analysis using services like AWS CloudWatch or the ELK Stack (Elasticsearch, Logstash, Kibana).
2. Monitoring and alerting the application's performance and overall health using technologies like Grafana, Prometheus, or Datadog.
3. A CI/CD pipeline for automated application development, testing, and deployment.


### Scalability:

Finally, depending on our development environment, we might employ the following strategies to scale this application with a rising dataset:

1. Implement horizontal scaling by adding extra ETL application instances to enable concurrent data processing.
2. Use appropriate indexing, partitioning, and sharding algorithms to improve database performance.
3. To handle high throughput and enable data streaming, use a message broker such as Apache Kafka or Amazon Kinesis.