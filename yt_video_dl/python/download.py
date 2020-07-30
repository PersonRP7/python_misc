import pafy, os

urls = [
    "https://www.youtube.com/watch?v=qJJgMIwqD4Q&list=RDqJJgMIwqD4Q&start_radio=1",
    "https://www.youtube.com/watch?v=fI569nw0YUQ&list=RDqJJgMIwqD4Q&index=11",
    "https://www.youtube.com/watch?v=zbYcte4ZEgQ",
    "https://www.youtube.com/watch?v=30pt2XUJKGQ",
    "https://www.youtube.com/watch?v=QB4bkfNbtTg",
    "https://www.youtube.com/watch?v=VBvxNhaEvHE",
    "https://www.youtube.com/watch?v=2Qs1J612nZs",

]

def download():
    for url in urls:
        video = pafy.new(url)
        best = video.getbest()
        best.download()

if __name__ == "__main__":
    download()