import yaml

# Load the YAML file
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Print the contents of the YAML file
print("YAML Configuration:")
print(config)

# Modify the 'debug' setting
config['settings']['debug'] = True

# Save the modified YAML back to the file
with open("config.yaml", "w") as file:
    yaml.safe_dump(config, file)

print("\nModified YAML Configuration:")
print(config)

# Validate YAML syntax
try:
    with open("config.yaml", "r") as file:
        yaml.safe_load(file)
    print("\nYAML syntax is valid.")
except yaml.YAMLError as exc:
    print("\nError in YAML syntax:", exc)


