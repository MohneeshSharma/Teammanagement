import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']


credentials = ServiceAccountCredentials.from_json_keyfile_name('keyfile.json', scope)
client = gspread.authorize(credentials)

spreadsheet = client.open('DataSheet') #change
worksheet = spreadsheet.worksheet('Sheet1') #this is to work on a specific sheet

print('------------------>connected to database<----------------------')

# TODO create add_user function (adds user to spreadsheet given name and serial numbers)
# TODO create remove_user function (removes user from spreadsheet given name and serial name)