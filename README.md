# telegram_bot
A command-line Python script to send a message to your personal Telegram bot.

## Setup and Usage

Read [this guide](http://www.theanalyticslab.nl/2018/06/24/telegram-messages/) to learn how to set up your own Telegram bot and get your token and chatID. This is heavily inspired from that guide, but generalises to a simple command-line tool.

You will need to install [python_telegram_bot](https://github.com/python-telegram-bot/python-telegram-bot).

The file _secrets_example.py_ shows the structure that your _secrets.py_ file should take. Fill in your token and chatID in the correct places and rename the file to _secrets.py_

To run the tool, navigate to the directory and type:
```
$ python gt_telegram_bot.py <optional personal message>
```
(assuming Python 3+ is your default installation)

To make this more convenient, make it an alias:
```
$ alias telebot='python <path>/gt_telegram_bot.py'
```
