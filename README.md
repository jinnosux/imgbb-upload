# imgbb-upload
A script that converts image from windows clipboard to (imgbb uploaded) link

* Prequisites:
- python 3.7+
- imgbb key (create an account on imgbb.com and get free api token. than, add it to .env file in this dir as imgbb-token = "paste-your-token-here" )
- pip -r requirements.txt

* Usage:
- In windows, use native `win key + shift + s` to select image from screen. 
- Run `python upload.py` and it will upload it to imgbb, and copy image link to clipboard
- Either delete or save image locally (in /images)