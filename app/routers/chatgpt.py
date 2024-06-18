from fastapi import APIRouter, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from services.chat_gpt_integration import ChatGPTIntegration


chatgpt_router = APIRouter(prefix="/chatgpt", tags=["ChatGPT"])


@chatgpt_router.post("/", response_class=JSONResponse, status_code=status.HTTP_200_OK)
async def ask_question(question: str):
    """
    # Ask a question to the ChatGPT API

    ## Request Body
    - `question`: The question to ask the ChatGPT API.

    ## Response
    - `response`: The response from the ChatGPT API.
    """
    response = ChatGPTIntegration.chat_response(question)

    return JSONResponse(content=jsonable_encoder(response))
