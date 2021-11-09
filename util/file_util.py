import os
def clean_pdf(directory: str):
    for x in os.listdir(directory):
        if x.endswith(".pdf"):
            os.remove(x)