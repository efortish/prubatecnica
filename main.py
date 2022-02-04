"""Prueba tecnica"""

#Project

from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine
from sql_app.hashing import Hash
from sql_app import token


#FastAPI
from fastapi import Depends, FastAPI, HTTPException

#sql alchemy
from sqlalchemy.orm import Session





models.Base.metadata.create_all(bind=engine)




app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/signup", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/all", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users



@app.post("/login",  tags=["Authentication"])
def login(request:schemas.LoginUser, db:Session=Depends(get_db)):
    user= db.query(models.User).filter(models.User.email==request.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Invalid Credentials")
    if not Hash.verify_password(request.password, user.password):
         raise HTTPException(status_code=404, detail="Invalid Password")

    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
    





