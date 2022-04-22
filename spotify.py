from telegram.ext import *
from telegram import *
import requests
import yt_dlp
from spotipy import *
import spotipy
import string
from youtube_search import YoutubeSearch
from os import path

def sptd(update, context: CallbackContext):
    Gamer = ''
    for char in context.args:
            if char !="[" + "'" + "]":
                Gamer += char
    if "https://open.spotify.com/playlist/" in Gamer:
        #Authentication - without user
        client_credentials_manager = SpotifyClientCredentials(client_id="efd7e80782a447ffac407b86c22e2bb5", client_secret="c54d167420da4495a4c1bf924800c100")
        sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
        playlist_link = Gamer
        playlist_URI = playlist_link.split("/")[-1].split("?")[0]
        track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Starting download of the playlist...\n MADE WITH ❤ BY @OnyyTheBest && @AmicioEspyy\n", parse_mode="html")    
        for track in sp.playlist_tracks(playlist_URI)["items"]:
            #URI
            track_uri = track["track"]["uri"]
            
            #Track name
            track_name = track["track"]["name"]
            
            #Main Artist
            artist_uri = track["track"]["artists"][0]["uri"]
            artist_info = sp.artist(artist_uri)
            
            #Name, popularity, genre
            artist_name = track["track"]["artists"][0]["name"]
            artist_pop = artist_info["popularity"]
            artist_genres = artist_info["genres"]
            
            #Album
            album = track["track"]["album"]["name"]
            
            #Popularity of the track
            track_pop = track["track"]["popularity"]
            print( "Song Found :  " +  track_name + " for " + update.message.from_user.username)
            results = list(YoutubeSearch(str(track_name), max_results=1).to_dict())[-1]
            results2 = str(results['url_suffix'])
            print(results2)
            results3 = "https://www.youtube.com" + results2
            ytdl = yt_dlp.YoutubeDL()
            info = ytdl.extract_info(results3, False)
            title1 = info.get('title', None)
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
            context.bot.send_audio(chat_id=update.effective_chat.id, audio=open(f'/home/ubuntu/Rinkoglionito/music/{title1}.mp3', 'rb'),
                                        caption="Share this bot to support us ❤️", title=f"{track_name} - {artist_name}", duration=f"{daudh}")
    else:
        track_name = ''
        for char in context.args:
            if char !="[" + "'" + "]":
                track_name += char
        print( "Song Found :  " +  track_name + " for " + update.message.from_user.username)
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