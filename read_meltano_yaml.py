import os
import yaml
import boto3
import sys

# Load the ssm_parameters.yml file from the parms_file directory
with open(
    os.getcwd() + "/parm_files/ssm_parameters.yml",
    "r",
) as data:
    parameters = yaml.safe_load(data)

# for x in find("value", parameters):
#     print(x)    

parameter_entries = {}
for parameter in parameters.get("parameters"):
    parameter_group = parameter.get("parameter_group")
    parameter_name = parameter.get("parameter_name")
    parameter_tags = parameter.get("tags")
    for plugin in parameter.get("plugins"):
        plugin_name = plugin.get("plugin_name")
        for setting in plugin.get("pluginsettings"):
            command = (
                "aws ssm put-parameter --name /{}/{}/{} --value {} --key-id 123 --type {} --description {} --tags {}".format(
                    parameter_group,
                    parameter_name,
                    plugin_name,
                    setting.get("value"),
                    setting.get("type"),
                    setting.get("description"),
                    parameter_tags,
                )
            )
            print(command)