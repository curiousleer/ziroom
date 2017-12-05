#*-coding:utf-8-*-
import requests
import re
import smtplib
import time
from email.mime.text import MIMEText

def get163mail(retries):
    _user = "sendemail@email.com"
    _pwd = "password"
    _to = "receiveemail@email.com"
    msg = MIMEText(" quickly!!!!")
    msg["Subject"] = "quicklyquickly!!!!"
    msg["From"] = _user
    msg["To"] = _to

    try:
        s = smtplib.SMTP_SSL("smtp.163.com", 465)
        s.login(_user, _pwd)
        s.sendmail(_user, _to, msg.as_string())
        s.quit()
        print "Send 163 Email Success!"
    except smtplib.SMTPException, e:
        print "retry.163mail..........,%s" % e
        if retries > 0:
            return get163mail(retries - 1)
        else:
            print "Send 163 Email Falied,%s" % e

print ("starting")
session = requests.session()
while 1:
    try:
        response_ziroom = session.get("http://www.ziroom.com/z/vr/60138527.html",
                                      headers={
                                          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0'})
        webpage_result = re.compile(r'title="配置中"')
        analyze_result = re.search(webpage_result, response_ziroom._content)
        if analyze_result:
            print "still processing! wait!"
	    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	    time.sleep(30)
        else:
            get163mail(5)
	    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	    print "quick get it!"
	    break
    except:
        print "fuck socket is closed, retry..."
        time.sleep(120)
        continue
