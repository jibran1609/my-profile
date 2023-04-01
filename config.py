#contact page
import smtplib
def send_mail (name,r_mail,phone,message):
    sender_mail = 'jibran_work@outlook.com'
    password = "Jibran@work"
    host = "smtp-mail.outlook.com"
    port = 587
    my_mail = "jibransheikh314@gmail.com"

    msg = f"""subject: website enquiry
    
    hello jibran,
    
    name:{name} 
    email: {r_mail}
    phonno: {phone}
    message: {message}
    htt
    """
        
    # msg1 = '''subject: auto reply
    # hello

    # Thanks so much for reaching out! This auto-reply is just to let you know… We received your email and will get back to you with a (human) response as soon as possible.

    # thanks
    # jibran
    # '''
    server = smtplib.SMTP (host,port)

    status_code ,response = server.ehlo()
    print (status_code,response)

    status_code ,response = server.starttls()
    print (status_code,response)

    status_code ,response = server.login(sender_mail,password)
    print (status_code,response)

    print ("login seccess")
    server.sendmail(sender_mail,my_mail,msg)
    # server.sendmail(sender_mail,r_mail,msg1)
    print ("sendmail seccess")
    server.quit()