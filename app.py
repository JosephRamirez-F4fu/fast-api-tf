from fastapi import FastAPI
from routes.task import router_task
app=FastAPI();

app.include_router(router_task)

