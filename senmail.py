import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'login.settings'

if __name__ == '__main__':

    subject, from_email, to = 'hellowolrd', 'walkly@163.com', '975990499@qq.com'
    text_content = 'hellowowlr'
    html_content = 'helloworld'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()