#!/usr/bin/env python
# coding: utf-8

# # Generate an OTP and Send it to user's email in python

# In[ ]:





# In[26]:


import smtplib             # smtplib is used to send emails.
import random              # random is used to generate random numbers for the OTP (One Time Password).
import email.message       # email.message is used to construct email messages.
import time                # time is used for working with time-related functions.
from tkinter import *      # tkinter is used to create the GUI for the OTP verification system.


# In[ ]:





# In[27]:


def generate_otp():
    return ''.join([str(random.randint(0,9)) for i in range(6)])
#generate_otp function genrates 6 digit otp




# In[28]:


def send_email(to_email, otp):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    from_email = 'ils.shubhamtomar@gmail.com'
    server.login(from_email, 'puxf rdjn xlne mgmh')
    msg = email.message.EmailMessage()
    msg['Subject'] = "OTP Verification"
    msg['From'] = from_email
    msg['To'] = to_email
    msg.set_content("Your OTP is: " + str(otp))
    server.send_message(msg)
    print('OTP sent')
    server.quit()
    return time.time()


# This function sends an email containing the OTP to the provided email address.
# It sets up an SMTP server to connect to Gmail.
# Logs into the Gmail account specified with the sender's email address and password.
# Constructs an email message with the subject "OTP Verification" and the OTP in the body.
# Sends the email and prints "OTP sent" to the console.
# Closes the server connection.


# In[29]:


def verify_otp():
    input_otp = OTP_input.get()
    if time.time() - sent_time <= 120:
        if input_otp == otp:
            result_label.config(text='Access Granted', fg='red',font = ('verdana', 15))
        else:
            result_label.config(text='Invalid OTP! Access denied', fg='red')
            retry = input('Do you want to resend OTP? (yes/no): ')
            if retry.lower() == 'yes':
                main()
            else:
                print('EXIT')
    else:
        result_label.config(text='Time limit exceeded! Please generate a new OTP', fg='red')
        
# Retrieves the OTP input from the user interface.
# Checks if the time since the OTP was sent is less than or equal to 120 seconds.
# If the time limit is not exceeded, it checks if the input OTP matches the generated OTP.
# If the OTP matches, it updates the result label with "Access Granted" in red color.
# If the OTP does not match, it prompts the user if they want to resend the OTP. If yes, it calls the main() function again.
# If the time limit is exceeded, it updates the result label with "Time limit exceeded! Please generate a new OTP" in red color. 


# In[30]:


def main():
    global sent_time, otp
    to_email = email_input.get()
    otp = generate_otp()
    sent_time = send_email(to_email, otp)
    result_label.config(text='')
    
# This function acts as the main entry point of the program.
# It gets the email address from the user interface.
# Generates a new OTP using generate_otp() function.
# Sends the OTP to the provided email address using send_email() function.
# Clears the result label.


# In[ ]:


window = Tk()
window.title('OTP Verification with Email')
window.minsize(500, 500)
window.configure(background='blue')

text_label = Label(window, text='OTP Verification window', fg='white', bg='blue')
text_label.pack()
text_label.config(font=('verdana', 24))

email_label = Label(window, text='Enter your Gmail', fg='white', bg='blue')
email_label.pack(pady=(15, 10))
email_label.config(font=('verdana', 15))

email_input = Entry(window, width=50)
email_input.pack(pady=(10, 10))

otp_button = Button(window, text='Get OTP', fg='black', bg='white', width=20, height=1, command=main)
otp_button.pack()

OTP_label = Label(window, text='Enter OTP', fg='white', bg='blue')
OTP_label.pack(pady=(15, 10))
OTP_label.config(font=('verdana', 15))

OTP_input = Entry(window, width=50)
OTP_input.pack(pady=(10, 10))

verify_button = Button(window, text='Verify OTP', fg='black', bg='white', width=20, height=1, command=verify_otp)
verify_button.pack()

result_label = Label(window, text='', fg='white', bg='blue')
result_label.pack(pady=(10, 10))

window.mainloop()

# Sets up a graphical user interface (GUI) window using Tkinter library.
# Creates labels, entry fields, and buttons for email input, OTP input, OTP generation, and OTP verification.
# Configures the appearance of the GUI elements such as font, color, and size.
# Binds the OTP generation and verification functions to their respective buttons.
# Starts the main event loop to display the GUI and handle user interactions.



# In[ ]:





# In[ ]:




