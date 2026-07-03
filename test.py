from config_loader import Config
from bot import Bot

cfg: Config = Config("/home/ahmed_void/python_projects/model_config_loader/config.json")
bot = Bot('jilali',cfg)
bot.train(500)
bot.train(550)
print(bot)