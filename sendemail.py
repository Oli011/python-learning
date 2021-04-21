def send(subject, context):
    #普通邮箱发送邮件
    from email.header import Header
    from email.mime.text import MIMEText
    from email.utils import parseaddr,formataddr
    import smtplib


    #获取用户数据、邮件内容、收件人地址、服务器地址
    from_addr = '*********'
    password = '*******'
    to_addr = '********'
    #填入收发件人信息即可
    #自定义收发件人和内容
    # from_addr = input('发件人：')
    # password = input('密码：')
    # To_addr = input('收件人：')
    # subject = input('主题：')
    # context = input('正文：')
    #定义一个将邮件地址格式化的函数
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    #将邮件内容转化为邮件对象
    msg = MIMEText(context,'html','utf-8')
    msg['Subject'] = Header(subject, 'utf-8').encode()
    msg['From'] = _format_addr('来自<%s>的邮件' % from_addr)
    msg['To'] = _format_addr('<%s>亲启'% to_addr)

    #连接服务器执行邮件发送任务
    smtp_server = 'smtp.partner.outlook.cn'
    smtp_port = 587
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()