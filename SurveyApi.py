from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import smtplib
from email.mime.text import MIMEText
from typing import List

app = FastAPI()

class SurveyQuestion(BaseModel):
    question: str
    choices: List[str]

class SurveyResponse(BaseModel):
    question: str
    answer: str
    
def send_email(subject: str, body: str, recipients: str):
    smtp_server = 'min server'
    smtp_port = 8000
    smtp_username = 'username'
    smtp_password = 'password'
    
    msg = MIMEText(body)
    msg ['Subject'] = subject
    msg ['From'] = smtp_username
    msg ['To'] = ','.join(recipients)
    
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)
        
def create_pull_request(question: str, answer: str):
    
@app.post("/survey/{email}")
async def submit_survey(email: str, survey_responses: List[SurveyResponse]):
    
    subject = "Survey Response"
    body = "Thanks for the answer.\n\n"
    for response in survey_responses:
        body += f"{response.question}: {response.answer}\n"
    send_email(subject, body, email)
    
    for response in survey_responses:
        create_pull_request(response.question, response.answer)
        
        return {"message": "Survey response submitted successfully."}
    
    
    
    