#Inefficient, reruns itself for every instance of a whitespace in every item.
#A more efficient way would be to remove every whitespace instance for every item.
import os

img_types = [
    ".png", ".jpg", ".jpeg"
]

def remove_whitespace():
    for img_type in img_types:
        for item in os.listdir("."):
            if img_type in item:
                for i in item:
                    if ord(i) == 32:
                        try:
                            os.rename(item, item.replace(" ", "_"))
                            remove_whitespace()
                        except FileNotFoundError as e:
                            print(f"Excepted {e} for {item}. Renaming ok.")
remove_whitespace()