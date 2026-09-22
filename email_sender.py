import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Step 1: Your details
your_email = "your_email@gmail.com"
your_password = "your_app_password"  # must be a Gmail App Password
recruiter_email = "john.doe@company.com"

# Step 2: Create email
msg = MIMEMultipart()
msg['From'] = your_email
msg['To'] = recruiter_email
msg['Subject'] = "Application for Data Analyst Role"

# Step 3: Email body
body = """
Dear John,

I am excited to apply for the Data Analyst role at ABC Corp.
Please find attached my customized resume highlighting relevant skills.

Looking forward to your response.

Best regards,
Moksha
"""
msg.attach(MIMEText(body, 'plain'))

# Step 4: Attach resume (use your customized resume file)
with open("resume.txt", "rb") as f:
    resume = MIMEApplication(f.read(), Name="resume.txt")
resume['Content-Disposition'] = 'attachment; filename="resume.txt"'
msg.attach(resume)

# Step 5: Send email via Gmail SMTP
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(your_email, your_password)
    server.send_message(msg)
    server.quit()
    print("✅ Email sent successfully!")
except Exception as e:
    print("❌ Error sending email:", e)
