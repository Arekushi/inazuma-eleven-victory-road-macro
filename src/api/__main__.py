import uvicorn
from config import settings
from src.api.app import app


def main():
    uvicorn.run(
        app,
        host=settings.API.host,
        port=settings.API.port,
        reload=settings.API.reload
    )


if __name__ == '__main__':
    main()
