import random
import re
import smtplib as smtp


# fintion to generate an OTP
def generateotp():
    otp = str(random.randint(100000, 999999))
    return otp


# funtion to take mail as input form user
def inputmail():
    email = input("Please Enter your Email: ")
    return email


# function to validate the email
def validatemail(mail):
    validation_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"  # validation using regular expression
    if re.search(validation_condition, mail):
        return True
    else:
        return False


# function to send mail
def sendmail(to, OTP):
    server = smtp.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('jaywebsitetest@gmail.com', 'jmjobvzzjbhzxbxz')
    str = f"""your Otp for login is {OTP}.
    Please don't share this OTP with anyone.
    Thank you."""
    server.sendmail('jaywebsitetest@gmail.com', to, str)
    print("Success✅🎉! OTP send successfully")


# main funtion
if __name__ == '__main__':
    otp = generateotp()  # calling generateotp funtion
    email = inputmail()  # calling inputmail function
    validation = validatemail(email)  # calling validatemail function
    if validation:  # if email is correct then send the mail
        sendmail(email, otp)
    else:
        print("You entered wrong email please❌ try again with proper email")
