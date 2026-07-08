from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, engine
import models
import schemas
import user_service

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.delete("/discounts/{discount_id}", response_model=schemas.DiscountResponse)
def delete_discount(discount_id: int, db: Session = Depends(get_db)):
    return user_service.delete_discount_service(db, discount_id)