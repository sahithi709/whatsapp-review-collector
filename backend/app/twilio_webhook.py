from fastapi import APIRouter, Form
from starlette.responses import PlainTextResponse
from .state import sessions, SessionState
from .crud import create_review

router = APIRouter()

@router.post("/whatsapp")
async def whatsapp_webhook(From: str = Form(...), Body: str = Form(...)):
    contact = From.replace("whatsapp:", "")
    message = Body.strip()

    if contact not in sessions:
        sessions[contact] = SessionState(stage="product")
        return PlainTextResponse("Hello 😊! Which product are you reviewing?")

    sess = sessions[contact]

    if sess.stage == "product":
        sess.product_name = message
        sess.stage = "name"
        return PlainTextResponse("Nice! What's your name?")

    if sess.stage == "name":
        sess.user_name = message
        sess.stage = "review"
        return PlainTextResponse("Great! Please type your review now ✨")

    if sess.stage == "review":
        review = await create_review(
            contact_number=contact,
            user_name=sess.user_name,
            product_name=sess.product_name,
            product_review=message
        )
        del sessions[contact]
        return PlainTextResponse("Thank you! 🎉 Your review has been saved.")
