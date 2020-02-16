from configparser import ConfigParser

class Linker():
    config = ConfigParser()
    config.read('sites.cfg')
    url_agify = config.get('AGIFY', 'url')