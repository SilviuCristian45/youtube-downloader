import multiprocessing.dummy
import subprocess
import pytube

ydl_opts = {'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192'}]}

def downloadMusic(url: str):
    #youtube-dl --extract-audio --audio-format mp3 [video]
    subprocess.run('youtube-dl --extract-audio --audio-format mp3 '+ url)

def readMusicList():
    with open("data.txt") as file:
        return [music[:-1] for music in file.readlines()]


if __name__ == '__main__':
    mode = input("""Enter a playlist (1) 
                    Load music from data.txt file (2)
    """)
    if mode == "2":
        music_list = readMusicList()
    else:
        playlistUrl = input("enter playlist url: ")
        playlistObj = pytube.Playlist(playlistUrl)
        music_list = playlistObj.video_urls
    with multiprocessing.dummy.Pool(5) as p:
            p.map(downloadMusic, music_list)

        
