# app/main.py
from pydantic import BaseModel
from fastapi import FastAPI
from app.tasks import add_numbers,send_email_task


app = FastAPI()

@app.post("/add")
def add(a: int, b: int):
    """
    Send task to Celery worker
    """
    task = add_numbers.delay(a, b)

    return {
        "task_id": task.id,
        "status": "Task submitted"
    }


class EmailRequest(BaseModel):
    to_email: str
    subject: str
    body: str

@app.post("/send-email")
def send_email(payload: EmailRequest):
    """
    Accepts email data and queues background email task.
    """
    task = send_email_task.delay(
        payload.to_email,
        payload.subject,
        payload.body
    )

    return {
        "message": "Email queued successfully",
        "task_id": task.id
    }