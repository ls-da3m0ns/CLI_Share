from sqlalchemy.orm import Session 
from helper.token_generator import generate_hashed_token
import sql_things.model as model, sql_things.schemas as schemas


def create_row(db: Session, info: schemas.CLI_main_scheme):
    hashed_token = generate_hashed_token(info.token)
    db_row = model.CLI_share(file_path = info.file_path,
                            file_name = info.file_name,
                            hashed_token = hashed_token,
                            new_file_name = info.new_file_name)
    db.add(db_row)
    db.commit()
    db.refresh(db_row)
    return db_row


def get_rows(db: Session, skip: int =0, limit: int = 100):
    return db.query(model.CLI_share).offset(skip).limit(limit).all()

def get_rows_bytoken(db: Session, hashed_token: str):
    return db.query(model.CLI_share).filter(model.CLI_share.hashed_token == hashed_token).first()
