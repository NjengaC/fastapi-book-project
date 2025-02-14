from fastapi import APIRouter

# Disable automatic trailing slash redirection
router = APIRouter(redirect_slashes=False)


@router.get("", tags=["stage2"])
async def stage2_endpoint():
    return {"message": "Stage 2 endpoint is live"}
