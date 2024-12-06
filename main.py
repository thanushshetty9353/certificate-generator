import os
import sys
from certificate_generator import add_text_to_image, convert_jpg_to_pdf, send_email
from excel import fetch_data_from_xlsx
from filename import certificateName, xlsxName, user_email , sender_passkey

def main():
    if not os.path.exists('./temp'):
        os.makedirs('./temp')

    file_path =  xlsxName() 
    data = fetch_data_from_xlsx(file_path)
    
    for i in data:
     
        if not i[1] or '@' not in i[2]:
            print(f"Invalid email address: {i[2]}")
            continue

        certificate_path = certificateName()
        input_image_path = os.path.join('certificates', certificate_path)
        temp_image_path = './temp/certificate.jpg'
        temp_pdf_path = "./temp/certificate.pdf"

        add_text_to_image(input_image_path, [i[1], i[2]], temp_image_path)
        
        if not os.path.exists(temp_image_path):
            print(f"File not found: {temp_image_path}")
            continue
        
        convert_jpg_to_pdf(temp_image_path, temp_pdf_path)
        
        name = i[1]
        email = i[2]
        print(email)
        subject = "🎉 Congratulations! Your Participation Certificate is Ready 🎓"

        body = f"""<!DOCTYPE html>
<html dir="ltr" xmlns="http://www.w3.org/1999/xhtml" lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>BGMI Event Participation</title>
  <style type="text/css">
    body {{
      margin: 0;
      padding: 0;
      font-family: Arial, sans-serif;
      background-color: white; /* Set background color to white */
      color: #161616;
    }}
    .container {{
      width: 100%;
      max-width: 600px; /* Adjusted max-width for the container */
      margin: 0 auto;
      padding: 20px; /* Added padding around the container */
    }}
    .card {{
      background-color: #1e1e1e;
      border-radius: 0px;
      padding: 20px;
      margin-bottom: 0px; /* Added margin between cards */
    }}
    .image-card {{
      max-width: 100%; /* Image card takes full width of container */
      border-radius: 12px;
      margin-bottom: 20px; /* Added margin below image */
    }}
    .image-card img {{
      width: 100%;
      border-radius: 12px;
    }}
    .text-content {{
      flex: 1;
    }}
    .text-content h1 {{
      text-align: center;
      color: #FFFFFF;
      font-size: 2em;
      margin-bottom: 20px;
    }}
    .text-content p {{
      max-width: 100%;
      line-height: 1.5;
      font-size: 1.2em;
      color: #FFFFFF;
      text-align: left;
    }}
    .text-content p span {{
      display: block;
      text-align: left;
      margin-top: 20px;
    }}
    .card:last-child {{
      margin-bottom: 0;
    }}
  </style>
</head>
<body>
  <div class="container">
    <!-- First Card -->
    <div class="card ax-center text-white mb-10">
      <div class="image-card">
        <img src="https://beebom.com/wp-content/uploads/2023/05/Untitled-design-4-5.jpg" alt="BGMI Event ">
      </div>
    </div>
    
    <!-- Second Card -->
    <div class="card ax-center text-white mb-10">
      <div class="text-content">
        <h1>Quiz Competition Participation</h1>
        <p>
          Dear {name},<br><br>
          We are thrilled to announce that your certificate for participating in the QUIZ Competition is now ready! 🌟 Please find the attached PDF certificate for your records.<br><br>
          Thank you for your enthusiasm and contributions. We hope you had an amazing time and look forward to your participation in future events!
        </p>
        <p>
          Best regards,<br>Team AIML
        </p>
      </div>
    </div>
  </div>
</body>
</html>


"""
        sender_email = user_email()
        passkey = sender_passkey()
        try:
            send_email(sender_email, passkey, email, subject, body, temp_pdf_path)
          
        except Exception as e:
            print(f"Failed to send email to {email} : {str(e)}")
            sys.exit(1)

if __name__ == "__main__":
    main()
