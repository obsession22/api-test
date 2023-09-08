# -*- coding:utf-8 -*-
import datetime
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

    def send_qq_email(self, zip_filename, summary, use_time, data_time):
        """
        发送邮件
        :param zip_filename:  附件名称
        :param summary: 测试用例执行结果
        :return:
        """
        msg = MIMEMultipart()
        msg['From'] = self.qq_email
        msg['To'] = self.to_email
        msg['Subject'] = '测试报告'
        case_total = summary.get('total', 0)
        case_passed = summary.get('passed', 0)
        case_failed = summary.get('failed', 0)
        case_skipped = summary.get('skipped', 0)
        case_error = summary.get('error', 0)
        case_collected = summary.get('collected', 0)

        # 邮件正文
        text = MIMEText(f"执行用例的数量：{case_total}\n"
                        f"收集到的用例：{case_collected}\n"
                        f"pass用例数量：{case_passed}\n"
                        f"failed用例数量：{case_failed}\n"
                        f"skipped用例数量：{case_skipped}\n"
                        f"error用例的数量：{case_error}\n"
                        f"执行时间：{use_time}秒\n"
                        f"任务执行时间：{data_time}", 'plain')
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
