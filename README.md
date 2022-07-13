# imgbb-upload
A script that uploads image from windows-native clipboard to imgbb, and copies the uploaded link back into clipboard

## Prequisites:
- python 3.7+
- imgbb free token (create an account on imgbb.com and get free api token. than, add it to .env file in this dir as imgbb-token = "paste-your-token-here" )
- pip -r requirements.txt

## Usage:
- In windows, use `win key + shift + s` open a Snip/Screenshot tool and select image from screen. 
- Run `python upload.py` and it will upload selected image to imgbb, and copy image link back into clipboard
- Either delete or save image locally (in /images)
