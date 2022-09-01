Welcome to the Schoology Assignment Checker! This file will serve as your user manual. Please follow the Setup and User
guide to start using the software.


Installation Guide:

1. Ensure that you have Python installed, any version 3.x should work. Install python from "https://www.python.org" if
   it is not installed on your system.

2. Open the Command Prompt, PowerShell, or any other Terminal. Type the command "python -m pip install requests" on
   windows or "./python -m pip install requests" if you are on linux or macOS (osx). This will install the library that
   is used to communicate with Schoology. Hit run and wait for the installation to finish.


Setup Guide:

1. The first step to using this program is to create a "login.env" file. This file should be created in the same
   directory (folder) as the "main.py" and this file ("README.txt"). To do this, you can simply create a text file and
   then change the name to "login.env". Be sure the file extension or the end of the name is ".env".

2. The second step is to fill in your information. The information stored in this file is only stored locally
   (on this computer), and I have no access to what is written in the "login.env" file. Please do not use any space
   characters (" ") unless instructed. Every time your are asked to write a new value to the file, please add a new line
   (hit the enter or return key on the keyboard). We will be going over what to write in this file in the following
   steps.

4. In this step we will be filling out the information needed for the messaging feature. Feel free to skip this step if
   you do not wish to use this feature. Be sure to disable this feature by writing "False" after "SEND_MESSAGE = " in
   the "main.py" file if you wish to disable this feature; otherwise, write "True". In the "login.env" file write
   "USER=" followed by your email address you wish to send the messages from. write "PWD=" followed by your email
   account password. Finally write "EMAIL=" followed by the email address you wish to receive the emails in.

5. In this step we will be filling out the information that will be needed for the program to communicate with
   Schoology. This step is necessary for the software to function. Please visit "https://app.schoology.com/api" and log
   in. Now copy the value in the box labeled "Your current consumer key". In the "login.env" file write "CONSUMER_KEY="
   followed by your consumer key that you just copied. Next copy the value in the box labeled "Your current consumer
   secret". In the "login.env" file write "CONSUMER_SECRET=" followed by the consumer secret that you just copied. Next
   navigate to your Schoology profile page. Look to the URL or link of your profile page (shown at the top of the
   browser where you would search). Copy the numerical value after "user/" and before "/info". In the "login.env" file
   write "USER_ID" followed by the numerical value you just copied.

10. Congratulations, you just finished setup! You are ready to start using the software.


Usage:

   1. To use the software, simply run the program with python installed. The program has to be running to send emails.

   2. To change any settings, simply open "main.py" using any text editor (Word, Notepad, TextEdit, etc) and read the
      instructions provided.

   3. If your carrier supports mail to text, you can set that up by setting your email to text address as the "EMAIL="
      value in "login.env". This will allow you to receive text messages rather than email messages.
      

Thank you for using Schoology Assignment Checker. I hope your experience was good.
- JChen 8/31/2022