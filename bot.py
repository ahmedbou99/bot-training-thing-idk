from config_loader import Config
class Bot:
    def __init__(self,name,config:Config):
        if not isinstance(config,Config):
            raise TypeError("config object is not in the right type")
        if not isinstance(name,str):
            raise TypeError("bot name should be a string")
        self.config = config
        self.name = name
        self.episodes_completed = 0
        return

    def train(self,training_eps):
        if training_eps<0:
            raise ValueError("training episodes should be positive")
        self.episodes_completed += training_eps

    def is_trained(self):
        return self.episodes_completed >= self.config.cfg_dict['episodes']

    def __repr__(self):
        return f'{self.name} | {self.episodes_completed}/{self.config.cfg_dict['episodes']}'        

