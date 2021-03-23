from helper.file_io import handle_file
from fastapi import FastAPI, File, UploadFile,Depends
from fastapi.responses import HTMLResponse, FileResponse
from helper.file_io import handle_file
from sqlalchemy.orm import Session 
from sql_things import clishare_db,schemas,model
from sql_things.database import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)
app = FastAPI() 

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

@app.get("/")
async def main():
    content = """
                    <body>
                    To know the usage visit github.com/ls-da3m0ns 
                    </body>
                """
    return HTMLResponse(content=content)

@app.post("/")
async def upload_file_func(file: UploadFile = File(...), db: Session=Depends(get_db)):
    content = await file.read()
    info = handle_file(file,content)
    info = schemas.CLI_create_scheme(**info)
    clishare_db.upload_file(db,info=info)
    return f'File_name: {info.file_name} Token: {info.token} '

@app.get("/{token}")
async def downlaod_file(token: int,db: Session=Depends(get_db)):
    print(token)
    info = clishare_db.get_file_bytoken(db,token)
    if info is None:
        return "Invalid Token"
    else:   
        return FileResponse(info.file_path+info.new_file_name,media_type='application/octet-stream',filename=info.file_name)
    

