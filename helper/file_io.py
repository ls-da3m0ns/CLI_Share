from os import write
import os
from datetime import datetime
from helper.token_generator import generate,filename_generate

def get_filename(file_cursor):
    return file_cursor.filename

def write_content(content,file_name,file_path):
    file = open(f"{file_path}{file_name}","wb")
    file.write(content)
    file.close()

def generate_file_path():
    path = "./files/" + str(datetime.utcnow().month) +"/" + str(datetime.utcnow().day)+"/"
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def handle_file(file_cursor,content):
    file_name = get_filename(file_cursor)
    file_path = generate_file_path()
    new_file_name = filename_generate(file_name)

    write_content(content,new_file_name,file_path)
    token = generate()
    return {"file_name":file_name,
            "file_path":file_path,
            "new_file_name": new_file_name,
            "token":token}



