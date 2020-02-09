# whatsapp-automation
It's a simple script to automatically send single message to multiple people. This script took input from a csv file. The csv file should contain the field Name. or else you can simple export all of your contacts to csv and give it as input to this script. 

You may think if it's simply sending smae text to multiple people, we can use whatsapp broadcast to send the message. I was thought the same. But whatsapp broadcast has it's own limits. We can't add more than 256 people on a broadcast and it don't have option to select all. So I was created this script automate the process. 

It's not fully automatic. It's a semi automatic script. You have to scan the QR-code manualy.

# Usage 

To use this script first you have to install selenium, chrome webdriver, and pandas.

  For Linux
  
    sudo pip3 install Selenium pandas

    sudo apt install chromium chromium-webdriver
  
to run this script,

    chmod +x whatsapp_script.py

    ./whasapp_script.py path/to/file.csv
