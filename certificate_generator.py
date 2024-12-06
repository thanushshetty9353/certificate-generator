import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from reportlab.pdfgen import canvas
import os
from PIL import Image, ImageDraw, ImageFont
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def add_text_to_image(image_path, text, output_path, font_path='./font/PTSerif-Italic.ttf'):
  
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font_size = 52
    if font_path:
        font = ImageFont.truetype(font_path, font_size)
    else:
        font = ImageFont.load_default(font_size)
    text_size = font.getbbox(text[0])
    x,y = (930-((text_size[2]-text_size[0])/2)), 700 
    draw.text((x, y), text[0], fill="black", font=font)
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    image.save(output_path)

def convert_jpg_to_pdf(jpg_file, pdf_file):
    img = Image.open(jpg_file)
    c = canvas.Canvas(pdf_file, pagesize=img.size)
    c.drawImage(jpg_file, 0, 0)
    c.save()
    img.close()
    os.remove(jpg_file)
    
def send_email(sender_email, sender_password, receiver_email, subject, body, pdf_file):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "html"))
    
    with open(pdf_file, "rb") as attachment:
        part = MIMEApplication(attachment.read(), _subtype="pdf")
        part.add_header(
            "Content-Disposition",
            f"attachment; filename=Certificate.pdf",
        )
        message.attach(part)

    text = message.as_string()

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, text)
            print(f"Email successfully sent to {receiver_email}")
    except Exception as e:
        print(f"Failed to send email to {receiver_email}: {str(e)}")
        

    