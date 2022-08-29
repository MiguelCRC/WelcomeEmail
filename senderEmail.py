import smtplib
import ssl
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

fileText = open('data.json')
newUsers = json.load(fileText)

for infoUser in newUsers['employees']:
    message = MIMEMultipart("alternative")

    message["Subject"] = "CRC ACCOUNTS - " + infoUser['name']
    message["From"] = sender_email
    receiver_email = infoUser["personalEmail"]

    if infoUser["userRemote"] != " ":
        profitTools = """\
      <p
        style="
          color: #2368c3;
          font-weight: bold;
          text-decoration: underline;
        "
      >
        Profit Tools
      </p>
      <p>
        User for Remote Desktop:
        <strong>{userRemote}</strong>
      </p>
      <p>
        Password for Remote Desktop:
        <strong>{userRemotePassword}</strong>
      </p>
      <p>
        Profit tools Password:
        <strong>{profitToolsPassword}</strong>
      </p>""".format(userRemote=infoUser["userRemote"], userRemotePassword=infoUser["userRemotePassword"], profitToolsPassword=infoUser["profitToolsPassword"])
    else:
        profitTools = " "

    if infoUser["threeplUsername"] != " ":
        threePl = """\
      <p 
        style="
          color: #2368c3;
          font-weight: bold;
          text-decoration: underline;
        "
      >
        3PL Account
      </p>
      <p>
        3PL Username:
        <strong>{threeplUsername}</strong>
      </p>
      <p>
        3PL Password Account:
        <strong>{threeplPasswordAccount}</strong>
      </p>
      <p>
        3PL GUID:
        <strong>{threeplGuid}</strong>
      </p>""".format(threeplUsername=infoUser["threeplUsername"], threeplPasswordAccount=infoUser["threeplPasswordAccount"], threeplGuid=infoUser["threeplGuid"])
    else:
        threePl = " "

    if infoUser["printerUniqueCode"] != " ":
        printerCode = """\
      <p 
        style="
          color: #2368c3;
          font-weight: bold;
          text-decoration: underline;
        "
      >
        Printer Unique Code
      </p>
      <p>
        Code:
        <strong>{printerUniqueCode}</strong>
      </p>
      """.format(printerUniqueCode=infoUser["printerUniqueCode"])
    else:
        printerCode = " "

    # Create the plain-text and HTML version of your message
    html = """\
      <!DOCTYPE html>
      <html lang="en">
        <head>
          <meta charset="UTF-8" />
          <meta http-equiv="X-UA-Compatible" content="IE=edge" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>Welcome to CRC BPO Solutions</title>
        </head>
        <body>
          <!-- HEADER -->
          <table
            border="0"
            cellpadding="0"
            cellspacing="0"
            width="100%"
            style="table-layout: fixed"
          >
            <tbody>
              <tr>
                <td bgcolor="#ffffff">
                  <div align="center" style="padding: 0px 15px 0px 15px">
                    <table border="0" cellpadding="0" cellspacing="0" width="600">
                      <tr>
                        <td style="padding: 20px 0px 30px 0px">
                          <table
                            border-left="1"
                            cellpadding="0"
                            cellspacing="0"
                            width="100%"
                            style="border: solid 1px #2d68c4"
                          >
                            <tr>
                              <td
                                bgcolor="white"
                                width="200"
                                align="left"
                                style="
                                  padding: 26px;
                                  border: solid 1px, 1px, 1px, 0px #666666;
                                "
                              >
                                <a href="#" target="_blank"
                                  ><img
                                    alt="CRC_Logo"
                                    src="http://crc.global/wp-content/uploads/2018/05/CRC-Global-2x.png"
                                    width="109"
                                    height="48"
                                    style="
                                      display: block;
                                      font-family: Helvetica, Arial, sans-serif;
                                      color: #666666;
                                      font-size: 16px;
                                    "
                                    border="0"
                                /></a>
                              </td>
                              <td
                                bgcolor="white"
                                width="400"
                                align="right"
                                style="padding: 24px"
                              >
                                <table border="0" cellpadding="0" cellspacing="0">
                                  <tr>
                                    <td
                                      align="right"
                                      style="
                                        padding: 0 0 5px 0;
                                        font-size: 14px;
                                        font-family: Arial, sans-serif;
                                        color: #666666;
                                        text-decoration: none;
                                      "
                                    >
                                      <span
                                        style="
                                          color: black;
                                          text-decoration: none;
                                          line-height: 1.2;
                                          text-transform: uppercase;
                                          font-size: 12px;
                                        "
                                        ><a href="mailto:crcbpo@crc.global"
                                          >crcbpo@crc.global</a
                                        ><br />1-888-800-3342<br />32 East Airline
                                        Hwy.kenner, LA 70062</span
                                      >
                                    </td>
                                  </tr>
                                </table>
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                    </table>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>

          <!-- ONE COLUMN SECTION -->
          <table
            border="0"
            cellpadding="0"
            cellspacing="0"
            width="100%"
            style="table-layout: fixed"
          >
            <tr>
              <td
                bgcolor="#ffffff"
                align="center"
                style="padding: 23px 15px 50px 15px"
              >
                <table border="0" cellpadding="0" cellspacing="0" width="500">
                  <tr>
                    <td>
                      <table width="100%" border="0" cellspacing="0" cellpadding="0">
                        <tr>
                          <td>
                            <!-- HERO IMAGE -->
                            <table
                              width="100%"
                              border="0"
                              cellspacing="0"
                              cellpadding="0"
                            >
                              <tbody>
                                <tr>
                                  <td>
                                    <table
                                      width="100%"
                                      border="0"
                                      cellspacing="0"
                                      cellpadding="0"
                                    >
                                      <tr>
                                        <td align="center">
                                          <img
                                            src="https://img.icons8.com/offices/100/000000/mail-contact.png"
                                            border="0"
                                            alt="contact_image"
                                            style="
                                              display: block;
                                              padding: 0;
                                              color: #666666;
                                              text-decoration: none;
                                              font-family: Helvetica, arial,
                                                sans-serif;
                                              font-size: 16px;
                                            "
                                          />
                                        </td>
                                      </tr>
                                    </table>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                          </td>
                        </tr>
                        <tr>
                          <td>
                            <!-- Appointment has been confirmed -->
                            <table
                              width="100%"
                              border="0"
                              cellspacing="0"
                              cellpadding="0"
                            >
                              <tr>
                                <td
                                  align="center"
                                  style="
                                    font-weight: bold;
                                    font-size: 24px;
                                    color: #316bc1;
                                    font-family: Helvetica;
                                    padding-top: 31px;
                                  "
                                >
                                  {name}
                                </td>
                              </tr>
                            </table>
                          </td>
                        </tr>
                        <tr>
                          <td align="center" style="padding: 37px 35px 0px 35px">
                            <h1>Welcome to CRC BPO Solutions</h1>
                            <h3>
                              From the IT & Development Department it is a pleasure
                            </h3>
                            <div>
                              <p>I hope this e-mail finds you well.</p>
                              <p>
                                I arranged your new office usernames and passwords.
                              </p>
                              <h4>These are your credentials:</h4>
                                <p
                                  style="
                                    color: #2368c3;
                                    font-weight: bold;
                                    text-decoration: underline;
                                  "
                                >
                                  Outlook Email
                                </p>
                                <p>
                                  Email User:
                                  <strong>{emailUser}</strong>
                                </p>
                                <p>
                                  Password:
                                  <strong>{emailPassword}</strong>
                                </p>
                                <p
                                  style="
                                    color: #2368c3;
                                    font-weight: bold;
                                    text-decoration: underline;
                                  "
                                >
                                  Ring Central
                                </p>
                                <p>
                                  Phone Number:
                                  <strong>{phoneNumber}</strong>
                                  ext
                                  <strong>{phoneExt}</strong>
                                </p>
                                <p>
                                  Password:
                                  <strong>{phonePassword}</strong>
                                </p>
                                {profitTools}
                                {threePl}
                                {printerCode}
                              <p>
                                Any other questions or issues you have, don’t hesitate
                                to ask !
                              </p>
                              <p>Thank you for your time!</p>
                              <h2>Welcome to our CRC Family.</h2>
                            </div>
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
          </table>

          <!-- FOOTER -->
          <table
            border="0"
            cellpadding="0"
            cellspacing="0"
            width="100%"
            style="table-layout: fixed"
          >
            <tbody>
              <tr>
                <td bgcolor="#ffffff">
                  <div align="center" style="padding: 0px 15px 0px 15px">
                    <table border="0" cellpadding="0" cellspacing="0" width="600">
                      <tr>
                        <td style="padding: 0px 0px 30px 0px">
                          <table
                            border="0"
                            cellpadding="0"
                            cellspacing="0"
                            width="100%"
                          >
                            <tr>
                              <td
                                width="400"
                                align="left"
                                style="
                                  border-top: 1px solid #d4d4d4;
                                  padding: 26px;
                                  font-size: 12px;
                                  color: #818c9e;
                                  font-family: Helvetica;
                                  padding-top: 46px;
                                "
                              >
                                2022 CRC Global Solutions - All Rights Reserved
                              </td>
                              <td
                                width="200"
                                align="right"
                                style="
                                  border-top: 1px solid #d4d4d4;
                                  padding: 24px;
                                  padding-top: 46px;
                                "
                              >
                                <table border=" 0" cellpadding="0" cellspacing="0">
                                  <tr>
                                    <td align="right">
                                      <img
                                        src="https://wareflexblob.blob.core.windows.net/wareflexblob/EmailTemplates/footer-icon.png"
                                        usemap="#image-map"
                                      />

                                      <map name="image-map">
                                        <area
                                          target=""
                                          alt="Facebook"
                                          title="Facebook"
                                          href="https://www.facebook.com/CRCGlobalSolutions/"
                                          coords="1,2,18,17"
                                          shape="rect"
                                        />
                                        <area
                                          target=""
                                          alt="Twitter"
                                          title="Twitter"
                                          href="https://twitter.com/crcgsolutions"
                                          coords="39,1,60,16"
                                          shape="rect"
                                        />
                                        <area
                                          target=""
                                          alt="Instagram"
                                          title="Instagram"
                                          href="https://www.instagram.com/crcgsolutions/"
                                          coords="80,3,94,15"
                                          shape="rect"
                                        />
                                      </map>
                                    </td>
                                  </tr>
                                </table>
                              </td>
                            </tr>
                          </table>
                        </td>
                      </tr>
                    </table>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </body>
      </html>      
    """.format(name=infoUser["name"], emailUser=infoUser["emailUser"], emailPassword=infoUser["emailPassword"], phoneNumber=infoUser["phoneNumber"], phoneExt=infoUser["phoneExt"], phonePassword=infoUser["phonePassword"],
               profitTools=profitTools, threePl=threePl, printerCode=printerCode,)

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)

    # Create secure connection with server and send email
    print("Enviando correo...")
    context = ssl.create_default_context()
    print("...........")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
        print("...........")
        print("Correo enviado a "+infoUser["name"])

fileText.close()
