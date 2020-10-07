import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

# 보내는 사람 정보
me = "wheatal123@gmail.com"
my_password = "dosqjxj0725#"

# 로그인하기
s = smtplib.SMTP_SSL("smtp.gmail.com")
s.login(me, my_password)

# 받는 사람 정보
you = "narafu2020@gmail.com"

# 메일 기본 설정
msg = MIMEMultipart("alternative")
msg['Subject'] = "Python Prj"
msg['From'] = me
msg['To'] = you

# 메일 내용
content = "파이썬 프로젝트 메일 보내기 테스트"
part2 = MIMEText(content, 'plain')
msg.attach(part2)

# 파일 첨부
part = MIMEBase('application', 'octet-stream')
with open("/StarburksMenu.xlsx", 'rb') as file:
    part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename="스타벅스.xlsx")
    msg.attach(part)

# 메일 보내기
s.sendmail(me, you, msg.as_string())

# 서버 끄기
s.quit()
