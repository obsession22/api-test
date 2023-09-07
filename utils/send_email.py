# -*- coding:utf-8 -*-
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


class Mail:
    qq_email = '1521988020@qq.com'  # 发件人邮箱账号
    qq_password = 'nyejyetrinifgbhf'  # 发件人邮箱授权码
    to_email = '1521988020@qq.com'  # 收件人邮箱账号，我这边发送给自己

    def send_qq_email(self,zip_filename):
        msg = MIMEMultipart()
        msg['From'] = self.qq_email
        msg['To'] = self.to_email
        msg['Subject'] = '邮件主题'

        # 邮件正文
        text = MIMEText('这是一封通过Python发送的邮件。', 'plain')
        msg.attach(text)

        try:
            attachment = open(zip_filename, 'rb')
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={zip_filename}')
            msg.attach(part)

            smtp_server = 'smtp.qq.com'
            smtp_port = 465
            server = smtplib.SMTP_SSL(smtp_server,smtp_port)
            server.login(self.qq_email,self.qq_password)
            server.sendmail(self.qq_email,self.to_email,msg.as_string())
            server.quit()  # 退出连接
            print("邮件发送成功")
        except Exception as e:
            print("发送失败", str(e))


# if __name__ == '__main__':
#     mail = Mail()
#     mail.send_qq_email()
