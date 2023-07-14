# Data Engineering Take Home: ETL off a SQS Queue

The main goal of this project is to build an ETL (Extract, Transform, Load) pipeline that will read JSON data from an AWS SQS Queue containing user login behaviour, mask fields that include personally identifiable information (PII), and publish the converted data to a PostgreSQL database.

# Project Setup

### Requirements

- Python 3.8+
- Docker
- Docker Compose
- pip
- AWS CLI (for local testing)

### Instructions to run the project

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