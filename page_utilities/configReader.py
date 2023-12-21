from configparser import ConfigParser


def readConfig(section, key):
    config = ConfigParser()
    config.read("..\\app_configuration_data\\conf.ini")
    return config.get(section, key)
