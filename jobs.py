from fastapi import APIRouter,UploadFile,File
from app.etl import process
from app.mailer import send_email
from app.s3_service import upload

router=APIRouter(prefix='/jobs')

@router.post('/run')
async def run(file:UploadFile=File(...)):
    path=f'/tmp/{file.filename}'
    with open(path,'wb') as f:
        f.write(await file.read())
    result=process(path)
    upload(path)
    send_email('client@gmail.com',str(result))
    return result.to_dict()
