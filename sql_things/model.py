from enum import unique
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Integer, DateTime
from sql_things.database import Base
import datetime

class CLI_share(Base):
    __tablename__ = "CLIshare_main"

    id = Column(Integer, primary_key=True, index=True)
    file_path = Column(String,index=True)
    hashed_token = Column(String)
    upload_date = Column(DateTime, default=datetime.datetime.utcnow)
    file_name = Column(String,default="None")
    new_file_name = Column(String,unique=True)