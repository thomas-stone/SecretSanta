## Secret Santa App

This is a simple secret santa app that allows users to generate a secret santa pairing

### Development Setup

Install python dependencies and enter virtual environment shell

```bash
pipenv install
pipenv shell
```

Install node dependencies

```bash
npm i --prefix ./frontend/
```

### Setup Local DynamoDB on port 8000

```bash
docker run \
    --name dynamodb \
    -p 8000:8000 \
    -d amazon/dynamodb-local \
    -jar DynamoDBLocal.jar
```

```bash
aws dynamodb create-table \
    --table-name users \
    --attribute-definitions \
        AttributeName=user_id,AttributeType=S \
    --key-schema \
        AttributeName=user_id,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --endpoint-url http://localhost:8000
```

```bash
aws dynamodb create-table \
    --table-name groups \
    --attribute-definitions \
        AttributeName=group_id,AttributeType=S \
    --key-schema \
        AttributeName=group_id,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --endpoint-url http://localhost:8000
```

### Running Dev Server

This is configured to run the frontend and backend as two separate services. Each of these commands should be run in a separate terminal instance. 

Run from the project root.

#### Frontend
```bash
npm run dev --prefix ./frontend/
```

#### Backend
```bash
python -m backend/main.py
```
#### DynamoDB (Docker)
If not running already, start a docker container running a local DynamoDB instance.
```bash
docker run \
    --name dynamodb \
    -p 8000:8000 \
    -d amazon/dynamodb-local \
    -jar DynamoDBLocal.jar
```