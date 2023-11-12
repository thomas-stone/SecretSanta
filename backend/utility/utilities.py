import boto3
import os


def get_dynamo_table(table_name):
    try:
        if os.environ.get('ENV', 'DEV') != 'PROD':
            raise EnvironmentError
        else:
            table = boto3.resource("dynamodb").Table(table_name)
    except EnvironmentError:
        table = boto3.resource("dynamodb", endpoint_url='http://localhost:8000').Table(table_name)

    return table