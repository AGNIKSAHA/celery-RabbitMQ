# app/celery_app.py

from celery import Celery
import os
from dotenv import load_dotenv

load_dotenv()

# Create Celery instance
celery_app = Celery(
    "worker",
    broker=os.getenv("RABBITMQ_URL"),
    backend="rpc://"  # stores results temporarily in RabbitMQ
)

# Optional configuration
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Asia/Kolkata",
    enable_utc=True,
)

celery_app.autodiscover_tasks(["app"])
