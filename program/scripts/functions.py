import pickle, smtplib, ssl, os

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart


def reset_data():
    dict1 = {
        "myself": 0
    }

    file = open("data/balance_sheet", "wb")
    pickle.dump(dict1, file)
    file.close()
    file = open("data/main_data", "rb")
    _data = pickle.load(file)
    file.close()
    return _data


def reset_profiles():
    dict1 = {
        "myself": ["Jym Patel", "jympatel@yahoo.com", True]
    }

    file = open("data/profiles", "wb")
    pickle.dump(dict1, file)
    file.close()


def help():
    help_doc = open("./docs/help.txt")
    print(help_doc.read())
    print("if you think help file is broken or incorrect please visit github.com/JymPatel/python")


def send_mail(username, add_balance):  
    print("Setting up Server ...")
    # smtp = smtplib.SMTP('smtp.gmail.com', 587)
    # smtp.ehlo()
    print("Starting Server ...")
    # smtp.starttls()
    # smtp.login(sender_email, password)
    print("Sending Mail ...")
    # msg = MIMEMultipart()
    # msg['Subject'] = "Balance Update"
    # msg.attach(MIMEText("Dear, " + name + "!\n"))
    # smtp.sendmail(from_addr=sender_email,
    #           to_addrs=reciver_email, msg=msg.as_string())
    print("Closing Server ...")
    # smtp.quit()
    print("Mail Sent Sucessfully")