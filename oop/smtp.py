import smtplib
from email.message import EmailMessage

class MyMail:
    def __init__(self, smtp_server, port, username, password):
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password

    def send(self, sender, receiver, subject, text, html):
        msg = EmailMessage()
        msg.set_content(text)
        msg.add_alternative(html, subtype="html")
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = receiver

        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.starttls()
            server.login(self.username, self.password)
            server.send_message(msg)

mail = MyMail(
    smtp_server="smtp.example.com",     # for example: smtp.gmail.com
    port=587,                           # SMTP default port
    username="youremail@example.com",   # your email
    password="YOUR_APP_PASSWORD"        # your app password
)

mail.send(
    sender="sender@example.com",         # your email
    receiver="receiver@example.com",     # receiver email
    subject="Test",                      # email subject
    text="Váš klient nepodporuje HTML.", # plain text
    html=""" 
    <html>
      <body>
        <h1>Ahoj</h1>
        <p>Toto je <strong>HTML</strong> e-mail.</p>
      </body>
    </html>
    """
)
