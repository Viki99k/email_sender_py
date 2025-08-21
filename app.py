# from email.message import EmailMessage
# import ssl
# import smtplib
# import streamlit as st

# email_sender = st.secrets["email_sender"]
# email_password = st.secrets["email_password"]  # Use Gmail App Password, not normal password

# email_r = input("Enter the email address of the hiring manager: ")
# position = input("Enter the position you are applying for: ")
# company = input("Enter the company name: ")
# job_board = input("Enter the job board where you found the job posting: ")

# email_receiver = email_r

# # ✅ Use f-string
# subject = f"Application for the post of {position} at {company}"

# # ✅ Use f-string + fix typo
# body = f"""
# Dear Hiring Manager,

# I am writing to apply for the {position} role at {company} that was advertised on {job_board}.
# I was impressed with {company}'s reputation as a leading player in the Tech Industry, and I believe my skills and experience would be a strong asset to your team.

# As a recent graduate and fresher, I have developed a strong foundation in JAVA, SQL, Python, Web Development, and Android Development through my academic projects, internships, and self-learning. I am eager to apply this knowledge to contribute effectively to your team. 

# Please find attached my Resume for your review. I would be happy to provide additional information or references upon request.

# Thank you for your consideration, and I look forward to the opportunity to discuss my application further.

# Sincerely,  
# Vikrant Kulkarni  
# 9325907915

# resume : https://drive.google.com/file/d/1vGkE-56D2NgIAXSoGMonn6wzWM4q4zfo/view?usp=drive_link
# """

# em = EmailMessage()
# em['From'] = email_sender   # ✅ fix capitalization
# em['To'] = email_receiver
# em['Subject'] = subject
# em.set_content(body)

# # ✅ Send securely
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
#     smtp.login(email_sender, email_password)
#     smtp.send_message(em)


import streamlit as st
from email.message import EmailMessage
import ssl, smtplib

# Secrets (from Streamlit Cloud → Settings → Secrets)
email_sender = st.secrets["email_sender"]
email_password = st.secrets["email_password"]

st.title("📧 Job Application Email Sender")

# Form inputs
email_r = st.text_input("Hiring Manager's Email Address")
position = st.text_input("Position you are applying for")
company = st.text_input("Company Name")
job_board = st.text_input("Job Board (e.g., LinkedIn, Naukri)")

if st.button("Send Application Email"):
    if email_r and position and company and job_board:
        # Subject & Body
        subject = f"Application for the post of {position} at {company}"
        body = f"""
        Dear Hiring Manager,

        I am writing to apply for the {position} role at {company} that was advertised on {job_board}.
        I was impressed with {company}'s reputation as a leading player in the Tech Industry, and I believe my skills and experience would be a strong asset to your team.

        As a recent graduate and fresher, I have developed a strong foundation in JAVA, SQL, Python, Web Development, and Android Development through my academic projects, internships, and self-learning. I am eager to apply this knowledge to contribute effectively to your team. 

        Please find my Resume attached for your review. I would be happy to provide additional information or references upon request.

        Thank you for your consideration, and I look forward to the opportunity to discuss my application further.

        Sincerely,  
        Vikrant Kulkarni  
        9325907915

        
resume : https://drive.google.com/file/d/1vGkE-56D2NgIAXSoGMonn6wzWM4q4zfo/view?usp=drive_link
        """

        # Create Email
        em = EmailMessage()
        em["From"] = email_sender
        em["To"] = email_r
        em["Subject"] = subject
        em.set_content(body)

        # Send Email
        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.send_message(em)
            st.success(f"✅ Email sent successfully to {email_r}")
        except Exception as e:
            st.error(f"❌ Failed to send email: {e}")
    else:
        st.warning("⚠️ Please fill in all fields before sending.")
