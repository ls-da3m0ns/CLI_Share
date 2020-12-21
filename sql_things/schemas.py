from datetime import date, datetime
from typing import List, Optional
from pydantic import BaseModel


class CLI_token_scheme(BaseModel):
    token: int

class CLI_create_scheme(CLI_token_scheme):
    file_name : str 
    file_path: str 
    new_file_name: str

class CLI_main_scheme(BaseModel):
    id: int 
    upload_date: Optional[datetime]
    hashed_token: str
    file_path: str
    file_name: str
    new_file_name: str
