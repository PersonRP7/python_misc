import os

def delete():
    directory = os.path.dirname(os.path.realpath(__file__))
    files = os.listdir(directory)

    for item in files:
        if item.endswith(".mp4"):
            os.remove(os.path.join(directory, item))

if __name__ == "__main__":
    delete()