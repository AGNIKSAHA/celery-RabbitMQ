# app/tasks.py
from app.celery_app import celery_app
from app.email_utils import send_email_smtp
from app.celery_app import celery_app
import time

@celery_app.task(bind=True)
def add_numbers(self, a: int, b: int) -> int:
    """
    Example background task.
    bind=True allows access to task instance (self)
    """
    time.sleep(5)  # simulate heavy processing
    return a + b


@celery_app.task(bind=True, autoretry_for=(Exception,), retry_kwargs={"max_retries": 3, "countdown": 10})
def send_email_task(self, to_email: str, subject: str, body: str) -> None:
    """
    Celery background task for sending email.

    - Retries automatically on failure
    - Runs outside request lifecycle
    """
    send_email_smtp(to_email, subject, body)