import yaml

def load_config(configPath=None):

    configPath = "./config.yml" if configPath is None else configPath

    with open(configPath, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            raise ValueError('Something went wrong loading the config.yml file. ' + exc)
