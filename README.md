# 🚀 FastAPI + Celery + RabbitMQ (Async Email via POST)

This project demonstrates how to send emails asynchronously using **Celery with RabbitMQ** in a **FastAPI** backend.  
The API accepts a POST request and queues the email to be sent in the background.

---

## 📌 Why This Architecture?

Sending emails synchronously blocks API requests and degrades performance.

This architecture provides:
- Non-blocking API responses
- Reliable background task execution
- Automatic retries on failure
- Better scalability and fault tolerance

---

## 🧱 High-Level Architecture

Client  
→ FastAPI (POST /send-email)  
→ Celery Producer  
→ RabbitMQ (Message Broker)  
→ Celery Worker  
→ SMTP Server (Email Sent)

---

## 📂 Project Structure

celery&RabbitMQ/
├── app/
│   ├── main.py           (FastAPI entry point)
│   ├── celery_app.py     (Celery configuration)
│   ├── tasks.py          (Background task definitions)
│   ├── email_utils.py    (Email sending logic)
│
├── venv/                 (Virtual environment)
├── .env                  (Environment variables)
├── requirements.txt
└── README.md

---

## ⚙️ Prerequisites

- Python 3.9 or higher
- RabbitMQ
- Virtual environment (venv)
- macOS or Linux

---

## 🐇 RabbitMQ Setup (macOS)

Install RabbitMQ:
brew install rabbitmq

Start RabbitMQ:
brew services start rabbitmq

Verify RabbitMQ:
rabbitmqctl status

RabbitMQ runs on:
- AMQP port: 5672
- Management UI: http://localhost:15672  
  Username: guest  
  Password: guest

---

## 🐍 Python Environment Setup

Create and activate virtual environment:
python -m venv venv  
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

---

## 🔐 Environment Variables

Create a `.env` file in the project root.

RABBITMQ_URL=amqp://guest:guest@localhost:5672//

SMTP_HOST=smtp.gmail.com  
SMTP_PORT=587  
SMTP_USERNAME=your_email@gmail.com  
SMTP_PASSWORD=your_app_password  
EMAIL_FROM=your_email@gmail.com

⚠️ For Gmail, use an App Password instead of your real password.

---

## 🧠 How Celery Works in This Project

- FastAPI acts as the task producer
- Celery pushes tasks into RabbitMQ
- RabbitMQ stores tasks in queues
- Celery workers consume and execute tasks
- Emails are sent via SMTP asynchronously

---

## ✉️ Email Sending Flow

1. Client sends POST request with email details
2. FastAPI validates the request
3. Celery task is queued in RabbitMQ
4. API responds immediately
5. Celery worker sends the email in background

---

## ▶️ Running the Application

Ensure RabbitMQ is running:
rabbitmqctl status

Start Celery worker:
celery -A app.celery_app.celery_app worker --loglevel=info

Start FastAPI server:
uvicorn app.main:app --reload

---

## 🧪 Testing the Email API

Use curl, Postman, or any REST client to call the POST endpoint.

Expected behavior:
- Immediate API response
- Email sent asynchronously
- Task execution visible in Celery logs

---

## 🚨 Common Issues & Solutions

Worker not starting → Check RabbitMQ status  
Task not executing → Ensure worker is running  
Circular import error → Use Celery autodiscovery  
Email not sent → Verify SMTP credentials  
Gmail auth error → Use App Password  

---

## 🏗 Production Recommendations

- Use SendGrid or AWS SES instead of raw SMTP
- Use Redis as Celery result backend
- Add Flower for Celery monitoring
- Run RabbitMQ with a dedicated user
- Dockerize all services

---

## 📌 Summary

FastAPI handles HTTP requests  
Celery processes background jobs  
RabbitMQ ensures reliable task delivery  
Email sending is asynchronous and scalable  

This setup is suitable for real-world production backends.
