from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from ..services import army_service
from ..core import security

router = APIRouter()

@router.post("/army-lists", response_model=schemas.ArmyList)
def create_army_list(
    army_list: schemas.ArmyListCreate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(security.get_current_active_user)
):
    return army_service.create_army_list(db=db, army_list=army_list, user_id=current_user.id)

@router.get("/army-lists", response_model=List[schemas.ArmyList])
def read_army_lists(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(security.get_current_active_user)
):
    army_lists = army_service.get_army_lists(db, skip=skip, limit=limit, user_id=current_user.id)
    return army_lists

@router.get("/army-lists/{list_id}", response_model=schemas.ArmyList)
def read_army_list(
    list_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(security.get_current_active_user)
):
    army_list = army_service.get_army_list(db, list_id=list_id)
    if army_list is None:
        raise HTTPException(status_code=404, detail="Army list not found")
    if army_list.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to access this army list")
    return army_list
