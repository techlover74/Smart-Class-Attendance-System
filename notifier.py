import smtplib
from email.mime.text import MIMEText

def notify_mentor(student_list, mentor_email="mentor@example.com"):
    body = f"Attendance Summary:\n\nPresent Students:\n" + "\n".join(student_list)
    msg = MIMEText(body)
    msg["Subject"] = "Class Attendance Report"
    msg["From"] = "attendance-system@example.com"
    msg["To"] = mentor_email
    
    # Send email (configure SMTP server)
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("your_email@gmail.com", "your_password")
        server.sendmail(msg["From"], [mentor_email], msg.as_string())
