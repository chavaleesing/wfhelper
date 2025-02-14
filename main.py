from fastapi import FastAPI
from wfhelper.api.router import router

app = FastAPI(title="My FastAPI Project", version="1.0")

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
