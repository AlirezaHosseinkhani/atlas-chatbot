# atlas-chatbot
This is a chat bot for atlas requests based on RASA AI


Rasa Version      :         3.6.20
Minimum Compatible Version: 3.5.0
Rasa SDK Version  :         3.6.2
Python Version    :         3.10.10
Operating System  :         macOS-14.4.1-x86_64-i386-64bit
Python Path       :         /Users/admin/Desktop/RASA ChatBot/atlas-chatbot/venv/bin/python3.10


To run it on your machine:

Make a directory and cd to that folder
  python3 -m pip install virtualenv    
  python3 -m venv .venv   
  install python 3.10
  python3.10 -m pip install rasa 
  install rasa requirements
  python 3.10 -m virtualenv venv

================================

Every time you want to run or train:
cd to directory
  source venv/bin/activate
  rasa init
  rasa train
  rasa run actions
  rasa shell
