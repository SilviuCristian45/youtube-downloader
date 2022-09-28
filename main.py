import multiprocessing.dummy
import multiprocessing
import subprocess
import pytube

def downloadMusic(url: str):
    subprocess.run('youtube-dl --extract-audio --audio-format mp3 -o "%USERPROFILE%\Desktop\smusicOutput\%(title)s.%(ext)s" '+ url)

def readMusicList():
    with open("data.txt") as file:
        return [music[:-1] for music in file.readlines()]


mode = input("""Enter a playlist (1) 
                Load music from data.txt file (2)
""")
numCores = multiprocessing.cpu_count()
if mode == "2":
    music_list = readMusicList()
else:
    playlistUrl = input("enter playlist url: ")
    playlistObj = pytube.Playlist(playlistUrl)
    music_list = playlistObj.video_urls
with multiprocessing.dummy.Pool(numCores) as p:
        p.map(downloadMusic, music_list)

        
