from bot import Bot
import sys
from invalid_learn_excp import InvalidLearnException
from invalid_batch import  InvalidBatchCntException
from invalid_episode import InvalidEpisodesException
from name_not_found import NameNotFoundException
from config_loader import Config
import json
import random


def main():
    try:
        if len(sys.argv)!=2:
            raise RuntimeError("wrong arguments")
        cfg = Config(sys.argv[1])
    except (json.JSONDecodeError,InvalidBatchCntException,InvalidLearnException,InvalidEpisodesException,NameNotFoundException,FileNotFoundError):
        print("the config file is missing some fields/corrupt/not found")   
        return 
    except RuntimeError:
        print('wrong arguments count')
        return
    #initializing
    bots = [Bot(f'bot{i}',cfg) for i in range(1,6)]
    #training
    for i in range(0,25):
        bot = random.choice(bots)
        bot.train(250)

    leaderboard = sorted(bots,key=lambda b:b.episodes_completed,reverse=True)

    for bot in leaderboard:
        print(bot)





if __name__ == '__main__':
    main()