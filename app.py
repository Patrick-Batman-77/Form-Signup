from flask import Flask, render_template, request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
sender_email = "sender_email"
sender_password = "sender_password"
receiver_email = "receiver_email"


app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
      f_name = ""
      l_name = ""
      email = ""
      if request.method == "POST":
            f_name = request.form["f_name"]
            l_name = request.form["l_name"]
            email = request.form["email"]
            
            subject = "Signup Requests"
            message = f"First_Name: {f_name}\nLast_Name: {l_name}\nEmail: {email}"

            # Create the MIME object
            msg = MIMEMultipart()
            msg["From"] = sender_email
            msg["To"] = receiver_email
            msg["Subject"] = subject
            msg.attach(MIMEText(message, "plain"))

            # Connect to Gmail's SMTP server
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()

            # Login to your Gmail account
            server.login(sender_email, sender_password)

            # Send the email
            server.sendmail(sender_email,             receiver_email, msg.as_string())

# Close the connection
            server.quit()
      return render_template('index.html')

if __name__=="__main__":
      app.run(debug=True, port=6969)
