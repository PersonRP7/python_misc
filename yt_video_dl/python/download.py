import pafy, os

urls = [
   
]

def download():
    for url in urls:
        video = pafy.new(url)
        best = video.getbest()
        best.download()

if __name__ == "__main__":
    download()