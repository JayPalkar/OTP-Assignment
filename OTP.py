import random
import smtplib as smtp


def sendmail(to, OTP):
    server = smtp.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('jaywebsitetest@gmail.com', 'jmjobvzzjbhzxbxz')
    server.sendmail('jaywebsitetest@gmail.com', to, OTP)
    print("OTP send")


if __name__ == '__main__':
    email = input("Please Enter your Email: ")
    otp = str(random.randint(100000, 999999))

    # print(otp)
    sendmail(email, otp)
