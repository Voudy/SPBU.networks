from irc_bot import IrcBot

options = {
    'server': 'chat.freenode.net',
    'port': 6667,
    'channel': '#botik',
    'nickname': 'Statham',
    'log_file': 'log.txt'
}

bot = IrcBot(**options)
bot.connect()
bot.listen()
