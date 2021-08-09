import smtplib
import ssl
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
      <!DOCTYPE html>
      <html lang="en">
        <head>
          <meta charset="UTF-8" />
          <meta http-equiv="X-UA-Compatible" content="IE=edge" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />

          <title>Welcome to CRC</title>
        </head>
        <body style="background-color: #cccc;">
          <div class="container" style="text-align: center; background-color: #ffff; margin-top: 5%; margin-bottom: 5%;">
            <!-- header -->
            <div class="row align-items-start header" style="background-color: #ffff; border-bottom: solid 5px #2368c3;">
              <div class="col">
                <img
                  src="http://crc.global/wp-content/uploads/2018/05/CRC-Global-2x.png"
                  alt="CRC"
                />
              </div>
              <div class="col"></div>
              <div class="col headerSpace" style="margin-top: 5%;">
                <a href="mailto:crcbpo@crc.global">Contact Us CRC BPO Honduras</a>
                <p></p>
                <p>32 EAST AIRLINE HWY KENNER, LA 70062</p>
              </div>
            </div>
            <!-- email body -->
            <div class="innerIcon" style="margin-top: 5%;">
              <img src="https://img.icons8.com/offices/200/000000/mail-contact.png" />
            </div>
            <h1 class="title" style="color: #2368c3; font-weight: bold; text-decoration: underline;">[NAME]</h1>
            <h1>Welcome to CRC BPO Solutions</h1>
            <h3>From the IT & Development Department it is a pleasure</h3>
            <div class="content">
              <p>I hope this e-mail finds you well.</p>
              <p>I arranged your new office usernames and passwords.</p>
              <h4>These are your credentials:</h4>
              <div class="email">
                <ul class="title" style="color: #2368c3; font-weight: bold; text-decoration: underline;">
                  Outlook Email
                </ul>
                <ul>
                  Email User:
                  <strong>[EMAIL]</strong>
                </ul>
                <ul>
                  Password:
                  <strong>[PASSWORD]</strong>
                </ul>
              </div>
              <div class="ringCentral">
                <ul class="title" style="color: #2368c3; font-weight: bold; text-decoration: underline;">
                  Ring Central
                </ul>
                <ul>
                  Phone Number:
                  <strong>[NUMBER]</strong>
                  ext
                  <strong>[EXTENSION]</strong>
                </ul>
                <ul>
                  Password:
                  <strong>[PASSWORD]</strong>
                </ul>
              </div>
              <div class="profitools">
                <ul class="title" style="color: #2368c3; font-weight: bold; text-decoration: underline;">
                  Profit Tools
                </ul>
                <ul>
                  User for Remote Desktop:
                  <strong>[REMOTE_USER]</strong>
                </ul>
                <ul>
                  Password for Remote Desktop:
                  <strong>[REMOTE_PASSWORD]</strong>
                </ul>
                <ul>
                  Profit tools Password:
                  <strong>[PROF_USERNAME]</strong>
                </ul>
              </div>

              <div class="closure">
                <p>Any other questions or issues you have, don’t hesitate to ask !</p>
                <p>Thank you for your time!</p>
                <br />
                <h2>Welcome to our CRC Family.</h2>
                <br />
              </div>
            </div>
            <!-- Footer -->
            <div class="row align-items-start footer" style="background-color: #ffff; border-top: solid 5px #2368c3; padding-top: 5%; padding-bottom: 5%; margin-top: 5%;">
              <div class="col">
                <p>&copy 2020 CRC Global Solutions - All Rights Reserved</p>
              </div>
              <div class="col"></div>
              <div class="col">
                <div class="row">
                  <div class="col">
                    <img class="iconSize" style="height: 30px; width: 30px; margin-left: 5%;" src="img/f_logo_RGB-Black_58.png" alt="facebook"/>
                    <img class="iconSize" style="height: 30px; width: 30px; margin-left: 5%;" src="img/glyph-logo_May2016.png" alt="instagram"/>
                    <img class="iconSize" style="height: 30px; width: 30px; margin-left: 5%;" src="img/2021 Twitter logo - black.png" alt="twitter"/>
                  </div>
                </div>          
              </div>
            </div>

          </div>
        </body>
      </html>
  """.format(name=tmpDict["name"], emailUser=tmpDict["emailUser"], emailPassword=tmpDict["emailPassword"], phoneNumber=tmpDict["phoneNumber"], phoneExt=tmpDict["phoneExt"], phonePassword=tmpDict["phonePassword"], userRemote=tmpDict["userRemote"], userRemotePassword=tmpDict["userRemotePassword"], profitToolsPassword=tmpDict["profitToolsPassword"])

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
