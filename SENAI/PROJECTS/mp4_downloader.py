from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print('ERROR')
    print('Download Successfully!')

link = str(input('Input the video link>> '))
Download(link)
