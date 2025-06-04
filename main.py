from fastapi import FastAPI
import uvicorn
from app.core.config import SessionLocal, engine

from app.routes.auth_routes import app as auth_app
from app.routes.doctor_routes import app as doctor_app
from app.routes.patient_routes import app as patient_app
from app.routes.appintment_routes import app as quotes_app
from app.routes.user_routes import app as user_app

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_app, tags=['Auth'], prefix='/auth')
app.include_router(doctor_app, tags=['Doctors'], prefix='/doctors')
app.include_router(patient_app, tags=['Patients'], prefix='/patients')
app.include_router(quotes_app, tags=['Quotes'], prefix='/quotes')
app.include_router(user_app, tags=['Users'], prefix='/users')


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
