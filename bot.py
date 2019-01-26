#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import the mysql client for python
import pymysql
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Create a connection object
dbServerName    = "127.0.0.1"
dbUser          = "alvaro"
dbPassword      = "123a123a"
dbName          = "tournament_bot"
charSet         = "utf8mb4"
cursorType      = pymysql.cursors.DictCursor

connectionObject   = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,
                                        db=dbName, charset=charSet,cursorclass=cursorType)

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def show_teams(bot, update):
    try:
        # Create a cursor object
        cursorObject = connectionObject.cursor()

        # SQL query string
        sqlQuery = "SELECT * from teams"   

        # Execute the sqlQuery
        cursorObject.execute(sqlQuery) 

        #Fetch all the rows
        rows = cursorObject.fetchall()

        for row in rows:
            bot.send_message(chat_id=update.message.chat_id, text=row)

    except Exception as e:
        print("Exeception occured:{}".format(e))
    finally:
        connectionObject.close()

def create_tournament(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="You are about to create a new tournament!!")
    bot.send_message(chat_id=update.message.chat_id, text="Selecting random teams...")

def update_next_match(bot, update):
    abs

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def answer(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="No contesto a tonterias")

#updater = Updater('462567247:AAEs76XLVZZeTesKJBShttI-XQASUic8yVU')
updater = Updater('710743623:AAEaG33UZd78fTEuZqRPIKmv8Dgn4C81-LM')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('show_teams', show_teams))
updater.dispatcher.add_handler(CommandHandler('update_next_match', update_next_match))
updater.dispatcher.add_handler(CommandHandler('create_tournament', create_tournament))
updater.dispatcher.add_handler(MessageHandler(Filters.text, answer))

updater.start_polling()
updater.idle()
