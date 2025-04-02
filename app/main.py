from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from app.database import engine, Base
from app.models.user import User
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.routers import resume


#databases
Base.metadata.create_all(bind=engine)

#routes
app.include_router(resume.router)


@app.get("/")
def read_root():
    return {"message": "AI Resume Tracker is live!"}
