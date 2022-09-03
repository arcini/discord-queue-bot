import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

queueCommandKey = "!queue"
addCommandKey = "add"
mistakeCommandKey = "removelast"
emptyCommandKey = "empty"

queueString = "Current queue:\n\n"
queueEnd = "\nTo empty the queue, type !queue empty"
queueFilename = "queue.pickle"
queue = []

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):    
    # ignore messages from self
    if message.author == client.user:
        return
    content = ""
    isQueueCommand = message.content.startswith(queueCommandKey)
    
    if isQueueCommand:
        msgSplit = message.content.split()

        # view queue
        if len(msgSplit) == 1 and msgSplit[0] == queueCommandKey:
            content = queueString
            for i, item in enumerate(queue):
                content += f"{i+1}. {item}\n"
            content += queueEnd

        if len(msgSplit) > 1:
            # remove last thing added to queue
            if msgSplit[1] == mistakeCommandKey:
                if len(queue) > 0:
                    item = queue[-1]
                    del queue[-1]
                    content = f"Deleted '{item}' from the queue."

            # add everything after command to the queue as one entry
            elif msgSplit[1] == addCommandKey:
                item = " ".join(msgSplit[2:])
                queue.append(item)
                content = f"Added '{item}' to the queue! To see the entire queue, type '!queue'"

            elif msgSplit[1] == emptyCommandKey:
                queue.clear()
                content = "Emptied queue."

            else:
                content = "Queuebot could not recognize that command."

            
    if len(content) > 0:    
        await message.channel.send(content)
