# Generate-an-OTP-and-Send-it-to-user-s-email-in-python


This GitHub repository contains the code for an OTP (One Time Password) verification system implemented in Python using the Tkinter library for creating a graphical user interface (GUI) and the smtplib library for sending emails. The system allows users to generate and verify OTPs via email for secure authentication purposes.

Features:

1. OTP Generation: The system generates a 6-digit OTP randomly using the `generate_otp()` function.

2. Email Sending: Utilizes the Gmail SMTP server to send emails containing the generated OTP to the provided email address.

3. OTP Verification: Users can input the received OTP into the GUI, and the system verifies its correctness within a time limit of 120 seconds.

4. User Interaction: The GUI interface enables users to input their email address, request OTP generation, input the received OTP, and verify its correctness.

Components:

- `otp_verification.py`: The main Python script containing the implementation of OTP generation, email sending, OTP verification, and GUI setup using Tkinter.
