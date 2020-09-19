import pafy, os

urls = [
    "https://www.youtube.com/watch?v=r_5DwObXHE0&list=RDMMuqw5fWER4Gs&index=2",
    "https://www.youtube.com/watch?v=80mbMU7xEqc&list=RDMMuqw5fWER4Gs&index=22",
    "https://www.youtube.com/watch?v=YGtXoOIJ7To",
    

]

def download():
    for url in urls:
        video = pafy.new(url)
        best = video.getbest()
        best.download()

if __name__ == "__main__":
    download()