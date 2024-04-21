import logging

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app import parameters
from app.routes import user

# uvicorn app.app:app --host 0.0.0.0 --port 5000 --reload

logging.basicConfig(level=logging.WARNING)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=parameters.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Health Check"])
def healthcheck():
    
    return JSONResponse(
        content={'msg': 'success'},
        status_code=status.HTTP_200_OK
    )

app.include_router(user.router)