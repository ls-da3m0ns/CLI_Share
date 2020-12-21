from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session 
import sql_things.crud as crud,sql_things.model as model,sql_things.schemas as schemas
from sql_things.database import SessionLocal, engine

def upload_file(db,info: schemas.CLI_create_scheme,):
    return crud.create_row(db,info=info)

def get_files(db,skip: int = 0, limit: int = 100, ):
    files = crud.get(skip,limit,db)
    return files

def get_file_bytoken(db,token: int):
    hashed_token = crud.generate_hashed_token(token)
    file_info = crud.get_rows_bytoken(db,hashed_token)
    return file_info
