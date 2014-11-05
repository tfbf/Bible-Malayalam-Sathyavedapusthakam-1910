import configparser


def parse_config(config_path):
    cp = configparser.SafeConfigParser()
    cp.read(config_path)
