from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from config import settings

def create_app() -> FastAPI:

    app = FastAPI(docs_url="/", title=settings.APP_NAME, version=settings.APP_VERSION)

    register_tortoise(
        app,
        db_url=settings.POSTGRES_URI,
        modules={"models": ["app.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
    register_views(app=app)

    return app


def register_views(app: FastAPI):
    from app.views import note_views
    app.include_router(note_views, prefix="/notes", tags=["Notes"])