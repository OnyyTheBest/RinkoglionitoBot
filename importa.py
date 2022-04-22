from telegram.ext import *
from telegram import *
import datetime
import userlist as usr
import requests

def ipinfo(update, context):
    chat_user_id = update.message.from_user.id
    print('User name id : ' , chat_user_id)
    chat_user_username = update.message.from_user.username
    print('@ of the ppl: ', chat_user_username)
    d=open("log.txt",'a',encoding="utf-8")
    if update.message.from_user.id in usr.OWNER:
        current_time = datetime.date.today()
        now = datetime.datetime.now()
        dt_string = now.strftime("%H:%M:%S")
        porco="Accesso consentito a: " + chat_user_username + " per il comando /ipinfo il giorno " + str(current_time) + " all'ora " + str(dt_string)
        print(f"Accesso consentito a: {chat_user_username} per il comando /ipinfo")
        hi = "https://ipinfo.io/json"
        stats = requests.get(hi)
        json_stats = stats.json()
        ip = json_stats["ip"]
        city = json_stats["city"]
        region = json_stats["region"]
        hostname = json_stats["hostname"]
        country = json_stats["country"]
        timezone = json_stats["timezone"]    
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"""
        ecco le mie info solo per te amore :D
        IP: {ip}
        Citta': {city}
        Regione: {region}
        Host: {hostname}
        Nazione: {country}
        Fuso orario: {timezone}
        """) 
        d.write(porco+"\n")
        d.close
    else:
        current_time = datetime.date.today()
        now = datetime.datetime.now()
        dt_string = now.strftime("%H:%M:%S")
        porco1="Accesso negato a: " + chat_user_username + " per il comando /ipinfo il giorno " + str(current_time) + " alle ore " + str(dt_string)
        d.write(porco1+"\n")
        d.close
        print(f"Accesso negato a: {chat_user_username} per il comando /ipinfo")
        context.bot.send_message(chat_id=update.effective_chat.id, text="<b>NON AVRAI MAI LE MIE INFO! STRONZO!</b>", parse_mode="html")
ipinfo_handler = CommandHandler('IPINFO', ipinfo)