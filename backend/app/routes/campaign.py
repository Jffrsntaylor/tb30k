from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from ..services import campaign_service
from ..core import security

router = APIRouter()

@router.post("/campaigns", response_model=schemas.Campaign)
def create_campaign(
    campaign: schemas.CampaignCreate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(security.get_current_active_user)
):
    return campaign_service.create_campaign(db=db, campaign=campaign, user_id=current_user.id)

@router.get("/campaigns", response_model=List[schemas.Campaign])
def read_campaigns(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(security.get_current_active_user)
):
    campaigns = campaign_service.get_campaigns(db, skip=skip, limit=limit, user_id=current_user.id)
    return campaigns

@router.get("/campaigns/{campaign_id}", response_model=schemas.Campaign)
def read_campaign(
    campaign_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(security.get_current_active_user)
):
    campaign = campaign_service.get_campaign(db, campaign_id=campaign_id)
    if campaign is None:
        raise HTTPException(status_code=404, detail="Campaign not found")
    if campaign.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to access this campaign")
    return campaign
