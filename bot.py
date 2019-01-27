#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import secrets
import random
import pdb

# Create a connection object
dbServerName    = "127.0.0.1"
dbUser          = "alvaro"
dbPassword      = "123a123a"
dbName          = "tournament_bot"
charSet         = "utf8mb4"
cursorType      = pymysql.cursors.DictCursor

connectionObject   = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,
                                        db=dbName, charset=charSet,cursorclass=cursorType)

original_teams = []

def fetch_teams():
    try:
        # Create a cursor object
        cursorObject = connectionObject.cursor()

        # SQL query string
        sqlQuery = "SELECT * FROM teams;"

        # Execute the sqlQuery
        cursorObject.execute(sqlQuery)

        #Fetch all the rows
        rows = cursorObject.fetchall()
        for row in rows:
            try:
                original_teams.append(row['team_id'])
            except Exception:
                print("Exception occurred fetching field 'team_id'")

    except Exception:
        print("Exception occurred in SQL Query fetching teams")

    #connectionObject.close()

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

    except Exception:
        bot.send_message(chat_id=update.message.chat_id, text="Exception occurred in SQL Query showing teams")
    # finally:
    #     connectionObject.close()

def create_tournament(bot, update):
    chosen_teams = []
    num_teams = 16
    bot.send_message(chat_id=update.message.chat_id, text="You are about to create a new tournament!!")
    bot.send_message(chat_id=update.message.chat_id, text="Selecting 16 random teams...")

    fetch_teams()

    while len(chosen_teams) < num_teams:
        try:
            random_choice = random.choice(original_teams)
            # Append if it's not already in the list
            if not chosen_teams.__contains__(random_choice):
                chosen_teams.append(random_choice)
        except Exception:
                print("Exception occurred choosing teams")

    try:
        # Create a cursor object
        cursorObject2 = connectionObject.cursor()

        # SQL query string
        table_uuid = secrets.token_hex(4)
        sqlQuery = "CREATE TABLE " + table_uuid + " (matchid varchar(25) not null, localteamid varchar(25) not null, visitorteamid varchar(25) not null, localuser varchar(25) not null, visitoruser varchar(25) not null, goalslocal int, goalsvisitor int, winner varchar(25));"
        print(sqlQuery)

        # Execute the sqlQuery
        cursorObject2.execute(sqlQuery)

        #Fetch all the rows
        rows = cursorObject2.fetchall()
        for row in rows:
            print (row['team_id'])

    except Exception as e:
        print("Exeception occured:{}".format(e))

    # finally:
    #     connectionObject.close()

    random.shuffle(chosen_teams)

    cursorObjectList = []

    for i in range(len(chosen_teams)):
        cursorObjectList.append(connectionObject.cursor())

    iters = 0
    while len(chosen_teams) > 0:
        try:

            team1 = chosen_teams[0]
            chosen_teams.pop(0)
            team2 = chosen_teams[0]
            chosen_teams.pop(0)
            match_uuid = secrets.token_hex(4)

            # SQL query string
            sqlQuery = "INSERT INTO " + table_uuid + " values ('" + match_uuid + "', '" + team1 + "', '" + team2 + "', 'alvaro', 'killo', 0, 0, 'None');"
            print(sqlQuery)

            # Execute the sqlQuery
            cursorObjectList[iters].execute(sqlQuery)
            print ("Team chosen")
            iters=iters+1

        except Exception as e:
            print("Exeception occured:{}".format(e))

def update_next_match(bot, update):
    abs

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def answer(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="No contesto a tonterias")

updater = Updater('710743623:AAEaG33UZd78fTEuZqRPIKmv8Dgn4C81-LM')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('show_teams', show_teams))
updater.dispatcher.add_handler(CommandHandler('update_next_match', update_next_match))
updater.dispatcher.add_handler(CommandHandler('create_tournament', create_tournament))
updater.dispatcher.add_handler(MessageHandler(Filters.text, answer))

updater.start_polling()
updater.idle()