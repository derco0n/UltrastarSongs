#!/usr/bin/python3

#
# parses a .csv-like file to download the the songs and extract audio to .mp3
# Artist - Songname;Youtube-Link
#
# derco0n, 2020/11

import youtube_dl
import csv
import os
from pathlib import Path


localpath = Path(os.getcwd())

with open('./songlist.txt', newline='') as csvfile:
        songreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in songreader:
                title = row[0]
                url = row[1]
                print("Working on: " + title + ": " + url)

                try:
                        targetdir = localpath / title

                        os.mkdir(targetdir)
                        os.mkdir(targetdir + "/odd")
                except Exception as e:
                        print("Creation of the directory %s failed: %s" % targetdir, str(e))
                else:
                        print("Successfully created the directory %s" % targetdir)
                        print("Download video")
                        ydl_opts = {
                                'format': 'bestvideo/best',
                                'outtmpl': str(targetdir) + '/%(title)s.%(ext)s',
                                'keepvideo': True,

                        }
                        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                                ydl.download([url])

                        print("Download Audio")
                        ydl_opts = {
                                'format': 'bestaudio/best',
                                'outtmpl': str(targetdir) + '/%(title)s.%(ext)s',
                                'keepvideo': False,
                                'postprocessors': [{
                                        'key': 'FFmpegExtractAudio',
                                        'preferredcodec': 'mp3',
                                        'preferredquality': '320',
                                }],

                        }
                        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                                ydl.download([url])

                        #break #DEBUG




