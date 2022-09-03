import os
import pickle
import atexit
import bot_definitions as bot

def onexit():
    with open(bot.queueFilename, 'wb') as fh:
        pickle.dump(bot.queue, fh, protocol=pickle.HIGHEST_PROTOCOL)

atexit.register(onexit)

if __name__ == "__main__": 
    #retrieve saved queue if it exists
    try:
        with open(bot.queueFilename, 'rb') as fh:
            bot.queue = pickle.load(fh)
    except FileNotFoundError:
        pass

    bot.client.run("<bot api token>")
