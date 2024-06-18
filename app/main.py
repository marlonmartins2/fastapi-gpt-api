from settings import settings

from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware

from version import __version__


app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
    version=__version__,
    contact={
        "name": "Marlon Martins",
        "url": "https://github.com/marlonmartins2",
        "email": "marlon.azevedo.m@gmail.com",
    },
    license_info={
        "name": "Copyright",
        "url": "https://github.com/marlonmartins2/fastapi-gpt-api/blob/master/LICENSE",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health_check")
def health_check():
    """
    Check if API is running.
    """
    return Response(status_code=status.HTTP_204_NO_CONTENT)
