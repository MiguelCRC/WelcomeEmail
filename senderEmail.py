import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "emailsender300@gmail.com"
password = 'Wareflex123'
receiver_email = "menriquez@crc.global"



fileText = str(open("demofile.txt", "r").read())
newUsers = fileText.split('\n')

for infoUser in newUsers:
  message = MIMEMultipart("alternative")
  
  tmp = infoUser.split(',')
  print(tmp)
  tmpDict = {
    "personalEmail": tmp[0],
    "name": tmp[1],
    "emailUser": tmp[2],
    "emailPassword": tmp[3],
    "phoneNumber": tmp[4],
    "phoneExt": tmp[5],
    "phonePassword": tmp[6],
    "userRemote": tmp[7],
    "userRemotePassword": tmp[8],
    "profitToolsPassword": tmp[9],
  }
  
  message["Subject"] = "CRC ACCOUNTS - " + tmpDict["name"]
  message["From"] = sender_email
  receiver_email = tmpDict["personalEmail"]

  # Create the plain-text and HTML version of your message
  html = """\
  <html>
    <body style="color:red;">
      <img src="https://img.icons8.com/offices/80/000000/mail-contact.png"/>
      <h1 class="hey">Hi,<br>      
        How are you?<br>
        <a href="http://www.realpython.com">Real Python</a> 

        has many great tutorials.
        <p>{name}</p>
        <p>{emailUser}</p>
        <p>{emailPassword}</p>
        <p>{phoneNumber}</p>
        <p>{phoneExt}</p>
        <p>{phonePassword}</p>
        <p>{userRemote}</p>
        <p>{userRemotePassword}</p>
        <p>{profitToolsPassword}</p>
      </h1>
      
    </body>
    
  </html>
  """.format(name=tmpDict["name"],emailUser=tmpDict["emailUser"],emailPassword=tmpDict["emailPassword"],phoneNumber=tmpDict["phoneNumber"],phoneExt=tmpDict["phoneExt"],phonePassword=tmpDict["phonePassword"],userRemote=tmpDict["userRemote"],userRemotePassword=tmpDict["userRemotePassword"],profitToolsPassword=tmpDict["profitToolsPassword"])

  # Turn these into plain/html MIMEText objects
  part1 = MIMEText(html, "html")

  # Add HTML/plain-text parts to MIMEMultipart message
  # The email client will try to render the last part first
  message.attach(part1)

  # Create secure connection with server and send email
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(
          sender_email, receiver_email, message.as_string()
      )