import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import parameters

# uvicorn app.app:app --host 0.0.0.0 --port 8000 --reload / python -m ?

if parameters.APP_MODE_OPTIONS['dev']:

    logging.basicConfig(level=logging.DEBUG)

else:

    logging.basicConfig(level=logging.WARNING)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=parameters.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router()