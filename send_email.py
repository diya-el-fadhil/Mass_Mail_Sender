import smtplib  # For sending email
from email.mime.text import MIMEText  # To format email text
from email.mime.multipart import MIMEMultipart  # To create email with subject and body

# Step 1: Enter your email credentials
sender_email = "spinxx360@gmail.com"  # Replace with your email
sender_password = "vmog qjgr ahso tzpz"  # Replace with your email password or App Password

# Step 2: List of recipient emails
recipient_emails = ["em.shinojeattath5112@gmail.com"]  # Add recipient emails

# Step 3: Email subject and body
subject = "Test Email from Me"
body = "Hello,\n\nThis is a test email sent using My code.\n\nBest regards,\nDEF"

# Step 4: Connect to the email server
smtp_server = "smtp.gmail.com"  # Gmail SMTP Server
smtp_port = 587  # Gmail uses port 587 for TLS

try:
    # Step 5: Set up the SMTP connection
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection
    server.login(sender_email, sender_password)  # Log in

    # Step 6: Send email to all recipients
    for recipient in recipient_emails:
        # Create the email message
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Send the email
        server.sendmail(sender_email, recipient, msg.as_string())
        print(f"Email sent to {recipient}")

    # Step 7: Close the connection
    server.quit()
    print("All emails sent successfully!")

except Exception as e:
    print(f"Error: {e}")
