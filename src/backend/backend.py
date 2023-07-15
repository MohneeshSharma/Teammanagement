import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('secrets/teammanagementsoftware-ae593bfb56b1.json', scope)
client = gspread.authorize(credentials)

spreadsheet = client.open('spreadsheet') #change 'spreadsheet with spreadsheet name
#worksheet = spreadsheet.worksheet('sheet1') this is to work on a specific sheet