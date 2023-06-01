from fastapi import FastAPI
from routes.task import router_task
app=FastAPI();

app.include_router(router_task)


if __name__ =="__main__":
    import  uvicorn 
    uvicorn.run(app,host="0.0.0.0",port=8001)    