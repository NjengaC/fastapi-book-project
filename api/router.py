from fastapi import APIRouter

from api.routes import books

api_router = APIRouter()
api_router.include_router(books.router, prefix="/books", tags=["books"])

# Only include /stage2 if ENABLE_STAGE2 is True.
from core.config import settings
if settings.ENABLE_STAGE2:
    from api.routes import stage2
    # This makes the endpoint available at /stage2
    api_router.include_router(stage2.router, prefix="/stage2", tags=["stage2"])
