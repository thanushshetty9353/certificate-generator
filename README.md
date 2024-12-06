# Certificate Generation and Email Automation 🎓📧

This project automates the generation of personalized certificates for participants and sends them via email. It uses data from an Excel file and creates certificates in PDF format, which are then sent as email attachments.  

---

## Features ✨
- **Dynamic Certificate Generation**: Names and other details are dynamically added to a certificate template.
- **PDF Conversion**: Certificates are converted from images to PDF format.
- **Email Automation**: Certificates are sent to participants via email.
- **Data Management**: Uses data from an Excel sheet for participant information.

---

## Requirements 🛠️

Before running the project, ensure you have the following installed:
- Python 3.x
- Required Python libraries:
  - `openpyxl` (for Excel file handling)
  - `Pillow` (for image processing)
  - `reportlab` (for PDF generation)
  - `smtplib` (for email automation)

Install the dependencies using:
```bash
pip install -r requirements.txt

Project Structure 📂
.
├── certificates/               # Folder containing certificate templates (e.g., Cream.png)
├── temp/                       # Temporary folder for intermediate files (auto-created)
├── certificate_generator.py    # Handles certificate creation and PDF conversion
├── excel.py                    # Fetches participant data from Excel file
├── filename.py                 # Configures file paths, user email, and password
├── main.py                     # Main script for the project
├── requirements.txt            # Required Python libraries
├── tune.xlsx                   # Excel file containing participant data
└── README.md                   # Project documentation

Usage 🚀
1. Prepare Your Files:
Excel File (tune.xlsx): Add participant details in the format:
Name	Email
John Doe	john.doe@email.com
Certificate Template: Place the certificate image (e.g., Cream.png) in the certificates folder.
2. Set Up Your Email:
Edit filename.py:
Replace the placeholder email with your sender email.
Replace the placeholder password with your sender email password (ensure less secure app access is enabled or use an app password).
3. Run the Project:
Execute the main script to generate certificates and send emails:


python main.py
Customization 🎨
Certificate Template: Edit Cream.png or use your own design.
Font and Position: Adjust the font size and position in certificate_generator.py for text alignment.
Email Content: Modify the email body in the main.py file for your event.
Known Issues 🐞
Invalid Emails: The program skips invalid email addresses and prints a warning.
Excel File Overwrite: Ensure the tune.xlsx file is updated or deleted after every use.
Contributions 🤝
Feel free to submit pull requests or report issues for improvements.

License 📄
This project is open-source and available under the MIT License.

Author ✍️
Thanush Shetty
Email:shettythanush9353@gmail.com
