from yt_dlp import YoutubeDL
import sys


def download(list, outputPath):
    opts = {
        'outtmpl': outputPath+'%(title)s-%(id)s.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': True
    }
    with YoutubeDL(opts) as ydl:
        ydl.download(list)


def main():
    links = []
    outputPath = sys.argv[1:][2] if sys.argv[1:][2] else "./"
    if int(sys.argv[1:][0]) == 1:
        inputPath = sys.argv[1:][1]
        with open(inputPath, "r") as f:
            links = f.read().splitlines()
    elif int(sys.argv[1:][0]) == 0:
        url = sys.argv[1:][1]
        links = [url]
    print(links)
    print(outputPath)
    download(links, outputPath)

def main2():
    links = []
    with open("./input.txt", "r") as f:
        links = f.read().splitlines()
        links = [x for x in links if x]
    download(links,'./output/')


if __name__ == "__main__":
    main2()
