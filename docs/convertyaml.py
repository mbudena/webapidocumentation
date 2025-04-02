import yaml
import json


with open("c:/Users/NoahMbude/webapi-docs - Copy/docs/OpenAPI.yaml", "r") as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

with open("c:/Users/NoahMbude/webapi-docs - Copy/docs/serviceSwagger.json", "w") as json_file:
    json.dump(yaml_data, json_file, indent=4)