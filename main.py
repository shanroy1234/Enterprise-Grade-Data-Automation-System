from fastapi import FastAPI
from app.routers import jobs,reports,admin
from app.scheduler import scheduler

app=FastAPI(title="Enterprise Data Automation Engine")

app.include_router(jobs.router)
app.include_router(reports.router)
app.include_router(admin.router)

@app.get("/")
def root():
    return {"message":"Enterprise Automation Engine Running"}
