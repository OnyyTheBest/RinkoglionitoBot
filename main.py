from distutils.cmd import Command
from telegram.ext import *
from telegram import *
import startt
import seri
import importa
import youtube
import spotify
import chk
import broadcast
import config
updater = Updater(token=config.Token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    startt.start(update,context)

def YAAA(update, context):
    startt.YAAA(update, context)

def BASTARDI(update, context):
    startt.BASTARDI(update,context)

def CMDS(update, context):
    startt.CMDS(update, context)

def rndmusci(update,context):
    seri.RNDMUSIC(update, context)

def info(update,context):
    seri.INFO(update, context)

def vip(update,context):
    seri.vip(update, context)

def ipinfo(update,context):
    importa.ipinfo(update, context)

def ytdl(update,context):
    youtube.ytdownload(update, context)

def sptd(update,context):
    spotify.sptd(update, context)

def oldupdate(update,context):
    startt.oldupdate(update, context)

def update(update,context):
    startt.oldupdate(update, context)

def cnf(update,context):
    startt.commandnotfount(update, context)

def bcast(update,context):
    broadcast.bcast(update, context)

start_handler = CommandHandler('start', start)
ya_handler = CommandHandler('yaaa', YAAA)
bastardi_handler = CommandHandler('bastardi', BASTARDI)
CMDS_handler = CommandHandler('cmds', CMDS)
rndmusic_handler = CommandHandler('rndmucic', rndmusci)
info_handler = CommandHandler('info', info)
vip_handler = CommandHandler('vip', vip)
ip_handler = CommandHandler('ipinfo', ipinfo)
ytd_handler = CommandHandler('ytd', ytdl)
sptd_handler = CommandHandler('sptd', sptd)
oldupdate_handler = CommandHandler('oldupdate', oldupdate)
update_handler = CommandHandler('update', update)
bcast_handler = CommandHandler('bcast', bcast)
commandnotfount_handler= MessageHandler(Filters.text, cnf)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(ya_handler)
dispatcher.add_handler(bastardi_handler)
dispatcher.add_handler(rndmusic_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(CMDS_handler)
dispatcher.add_handler(vip_handler)
dispatcher.add_handler(ip_handler)
dispatcher.add_handler(ytd_handler)
dispatcher.add_handler(sptd_handler)
dispatcher.add_handler(bcast_handler)
dispatcher.add_handler(oldupdate_handler)
dispatcher.add_handler(update_handler)
dispatcher.add_handler(commandnotfount_handler)
dispatcher.run_async
updater.start_polling()
print("[TELEGRAM BOT] IN ACTIONS NOW!!!")
