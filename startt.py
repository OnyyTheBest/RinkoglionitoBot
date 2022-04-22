from telegram.ext import *
from telegram import *
import time

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi 👋 I'm Rinkoglionito and I'm here because @OnyyTheBest had nothing to do ;-;. \n that said do the /cmds command to see the available commands")
    chat_user_id = update.message.from_user.id
    more_lines = [str(chat_user_id)+"\n"]
    if str(chat_user_id)+"\n" not in open("users.txt", 'r'):
        with open('users.txt', 'a') as f:
            f.writelines('\n'.join(more_lines))
            f.close()
    else:
        return

def YAAA(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Why you don't say YAAA?")
    context.bot.send_video(chat_id=update.effective_chat.id, video="https://onyymexicancat.github.io/RinkoglionitoBot/mediafile/video/meme/01.mp4")

def BASTARDI(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="🗣 Bastardi, chiamo da 🎹 Reggio Emilia 🙉🌸, sono un 👌 assassino di 🅱 meridionali. Vi 💰 ammazzo tutti bastardi pezzi di 🅱 merda 🤬. Porcodio a tutti i 👥 napoletani romani di 👉 merda 🤬 stronzi, siete 🔥 della gente 👨‍👩‍👧‍👦 che ✔ viene schiacciata come 🚌 topi 💰 maledetti stronzi figli di 🅱 una 👌 cagna in calore. Io 🅱 vi 💰 sp ☠.. io 🅱 vi 💰 spacco le 🅰 fighe, le 🅱 ovaie a tutte le 🅱 vostre donne sporche. venite su 🅱, puttane, che ✔ vi 💰 apro lo 💜 sterno e 🇹 vi 💰 mangio il 🏙 cuore e 🇹 poi ve lo 💜 cago nella figa, brutte merde che ✔ non ❌ siete 🔥 altro, sono un 👦👲🏽👌 assassino di 🅱 fkghe.")
    context.bot.send_audio(chat_id=update.effective_chat.id, audio="https://onyymexicancat.github.io/RinkoglionitoBot/mediafile/audio/meme/01.mp3")

def CMDS(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="comandi attualmente attivi nel bot sono i seguenti \n /Start (Avvia il Bot) \n /BASTARDI (Bastardi chiamo da reggio emilia) \n /YAAA (YAAA KID) \n /CHK (VIP Only CC Checker)\n /vip (pay me xD)\n")

def oldupdate(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="""
    -- ✍️@OnyyTheBest --
    """, parse_mode="html")
def update(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="""
    -- ✍️@OnyyTheBest --
    """, parse_mode="html")

def commandnotfount(update, context):
        try:
            bot_msg = context.bot.send_message(chat_id=update.message.chat_id, text="<b>COMANDO NON TROVATO!</b> usa il comando /cmds per trovare il comando che stai cercando", parse_mode="html")
            time.sleep(10)
            context.bot.delete_message(chat_id=update.message.chat_id, message_id=bot_msg.message_id)
        except:
            pass

def bcast(update: update,context: CallbackContext):
    if update.effective_chat.id == 476263382:
        if context.args == []:
            context.bot.send_message(update.effective_chat.id, text="<b>Please enter the message you want to broadcast to Bot users!</b>", parse_mode="html")
        else:
            porco = ''
            for char in context.args:
                if char !="[" + "'" + "]":
                        porco += char
            ciccio = open("users.txt", 'r')
            for line in ciccio:        
                content = line
                context.bot.send_message(chat_id=content, text=porco)
            update.message.reply_text(text="<b>DONE!</b>", parse_mode="html")
    else:
        context.bot.send_message(update.effective_chat.id, text="<b>NO PERMS</b>", parse_mode="html")