import os
import yaml
import boto3
import sys

# class SSMParameters(object):
#     """
#     Custom class used to hold configuration defining a SSM Parameter Entry for a Meltano Environment Variable.

#     On initialisation, create display the objects
#     """
#     def __init__(self, parameter: dict, **kwargs) -> None:


# Check the AWS Credentials are present
if boto3.session.Session().get_credentials() is None:
    print('Please provide Boto3 credentials, e.g. via the AWS_ACCESS_KEY_ID '
          'and AWS_SECRET_ACCESS_KEY environment variables.')
    sys.exit(-1)

session = boto3.Session(region_name='ap-southeast-2')
ssm = session.client('ssm')

ssm_parameter = ssm.get_parameter(Name='/meltano/tap-mssql--provation/tap_mssql__provation__select', WithDecryption=True)
print(ssm_parameter['Parameter']['Value'])

ssm_parameters = ssm.get_parameters_by_path(Path='/meltano/tap-mssql--provation', Recursive=True, WithDecryption=True)

for ssm_parameter in ssm_parameters.get("Parameters"):
    print(ssm_parameter)
    print(ssm_parameter.get("Name"))
    print(ssm_parameter.get("Value"))
    print(ssm_parameter.get("Type"))
    print(ssm_parameter.get("Description"))

# print(ssm_parameters['Parameters']['Name'])
# print(ssm_parameters['Parameters']['Value'])
# print(ssm_parameters['Parameters']['Type'])