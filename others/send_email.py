import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import dotenv_values
import json

config = dotenv_values(".env")

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

create_table = """create table if not exists users (
                    name text NOT NULL);"""
c.execute(create_table)

def get_total_and_last_user():
    cur = conn.cursor()
    last_user = cur.execute('select * from users')
    users = last_user.fetchall() 
    last_user = users[-1][0]
    total = len(users)
    return f'New user is commin up: {last_user}, Total is {total}'

def send_email_message():
    recipients = json.loads(config.get('RECIPIENTS'))
    gmail_user = config.get('GMAIL_USER')
    gmail_password = config.get('GMAIL_PASSWORD')

    msg = MIMEMultipart()

    msg['From'] = gmail_user
    msg['To'] = ', '.join(recipients)
    msg['Subject'] = 'New User on Irrengular Verbs Bot'
    body = get_total_and_last_user()
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.send_message(msg)
        server.quit()
    except Exception as exceptions:
        print(f'Error: {exceptions}')

def new_user(user_name):
    c.execute("INSERT INTO users (name) VALUES (?)", (user_name,))
    conn.commit()

def main():
    new_user('demo_user')
    send_email()

if __name__ == '__main__':
    main()

