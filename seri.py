from telegram.ext import *
from telegram import *
import random
import userlist as usr

def RNDMUSIC(update: Update, context: CallbackContext):
    gamer = random.randrange(1,174)
    oronzo = "https://onyymexicancat.github.io/RinkoglionitoBot/mediafile/audio/rndsong/("
    porco = ").mp3"
    print(oronzo + str(gamer) + porco)
    context.bot.send_audio(chat_id=update.effective_chat.id, audio=oronzo + str(gamer) + porco)

def INFO(update: Update, context: CallbackContext):
    keyb = InlineKeyboardMarkup([
    [InlineKeyboardButton("Profile :D",url="https://www.instagram.com/OnyyTheMexicanCat/")]
    ])
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bot Developer @OnyyTheBest \n don't spam me in dm pls ;-; \n to see bot commands do command /CMDS \n soon new commands", reply_markup=keyb)
    return keyb
info_handler = CommandHandler('info', INFO)

def vip(update, context: CallbackContext):
    chat_user_id = update.message.from_user.id
    print('User name id : ' , chat_user_id)
    chat_user_username = update.message.from_user.username
    print('@ of the ppl: ', chat_user_username)
    if update.message.from_user.id in usr.gamerciccio:
        context.bot.send_message(update.effective_chat.id, text="Grazie per avermi pagato... pezzo di merda!")
    else:
        
        keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Profile :D",url="t.me/OnyyTheBest")]
        ])
        context.bot.send_message(update.effective_chat.id, text="Contattami per info / prezzo ;D", reply_markup=keyboard)
        return keyboard
vip_handler= CommandHandler('vip', vip)