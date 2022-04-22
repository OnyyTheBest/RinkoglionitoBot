from telegram.ext import *
from telegram import *
import requests
import yt_dlp
from youtube_search import YoutubeSearch
import os
from os import path

def ytdownload(update: Updater, context: CallbackContext):
    if context.args == []:
        context.bot.send_message(chat_id=update.effective_chat.id, text="⚠️<b>Impossibile trovare il video,\ninserisci un url dopo /ytd!</b>⚠️", parse_mode="html")
    elif "https://www.youtube.com/watch?" or "https://youtu.be" not in context.args:
        track_name = ''
        for char in context.args:
            if char !="[" + "'" + "]":
                track_name += char
                print( "Song Found :  " + track_name  + " for " + update.message.from_user.username)
        results = list(YoutubeSearch(str(track_name), max_results=1).to_dict())[-1]
        results2 = str(results['url_suffix'])
        print(results2)
        results3 = "https://www.youtube.com" + results2
        ytdl = yt_dlp.YoutubeDL()
        info = ytdl.extract_info(results3, False)
        title1 = info.get('title', None)
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"<b>Starting download of </b>{title1}<b>...</b>", parse_mode="html")
        daudh = info.get('duration', None)
        ydl_optssx = {
                    "format": "bestaudio/best",
                    "outtmpl": f"/home/ubuntu/Rinkoglionito/music/{title1}.mp3",
                    "geo_bypass": True,
                    "nocheckcertificate": True,
                    "quiet": True,
                    "no_warnings": True,
                    }
        x = yt_dlp.YoutubeDL(ydl_optssx)
        dloader = x.download([results3])
        dloader
        xyz = path.join("music", f"{info['title']}.{info['ext']}")
        context.bot.edit_message_text(chat_id=update.effective_chat.id, message_id=update.message.message_id + 1, text=f"Download complete, starting upload...\n MADE WITH ❤ BY @OnyyTheBest && @AmicioEspyy\n", parse_mode="html")
        context.bot.send_audio(chat_id=update.effective_chat.id, audio=open(f'/home/ubuntu/Rinkoglionito/music/{title1}.mp3', 'rb'),
                                        caption="Share this bot to support us ❤️", title=f"{title1}", duration=f"{daudh}")    
    else:
        url = ''
        for char in context.args:
                if char !="[" + "'" + "]":
                    url += char
        
        savepath = '/'.join(os.getcwd().split('/')[:3]) + '/music/'
        
        ytdl = yt_dlp.YoutubeDL()
        info = ytdl.extract_info(url, False)
        title = info.get('title', None)
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"<b>Starting download of {title}...</b>", parse_mode="html")
        ydl_optssx = {
            "format": "bestaudio/best",
            "outtmpl": f"/home/ubuntu/Rinkoglionito/music/{title}.mp3",
            "geo_bypass": True,
            "nocheckcertificate": True,
            "quiet": True,
            "no_warnings": True,
        }
        try:
            x = yt_dlp.YoutubeDL(ydl_optssx)
            dloader = x.download([url])
        except Exception as y_e:
            return print(y_e)
        else:
            context.bot.edit_message_text(chat_id=update.effective_chat.id, message_id=update.message.message_id + 1, text=f"Download complete, starting upload...\n MADE WITH ❤ BY @OnyyTheBest && @AmicioEspyy\n", parse_mode="html")
            dloader
        xyz = path.join("music", f"{info['title']}.{info['ext']}")
        cixao = open(f"/home/ubuntu/Rinkoglionito/music/{title}.mp3", 'rb')
        daudh = info.get('duration', None)
        context.bot.send_audio(chat_id=update.effective_chat.id, audio=cixao, duration=daudh)
        return xyz
ytdownload_handler = CommandHandler('ytd', ytdownload, pass_args=True)
