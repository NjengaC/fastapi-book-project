from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["stage2"])
async def stage2_endpoint():
    return {"message": "Stage 2 endpoint is live"}
