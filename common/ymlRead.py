import yaml
from main import ENVIO, Dri


class YamlRead:
    @staticmethod
    def env_config():
        with open(file=f'{Dri}\envConfig\{ENVIO}\config.yml', mode='r', encoding='utf-8') as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    @staticmethod
    def data_config():
        with open(file=f'{Dri}/data/interface_config.yml', mode='r', encoding='utf-8') as f:
            return yaml.load(f, Loader=yaml.FullLoader)
