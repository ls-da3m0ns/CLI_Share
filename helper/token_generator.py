from random import randint

def generate():
    return randint(1000,9999)

def filename_generate(file_name):
    return file_name+str(randint(1000,9999))
     
def generate_hashed_token(token):
    return str(token)