# spreadsheet_utils.py

import gspread
from oauth2client.service_account import ServiceAccountCredentials


def get_spreadsheet():
    scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('keyfile.json', scope)
    client = gspread.authorize(credentials)
    spreadsheet = client.open('DataSheet')
    return spreadsheet

def add_data_to_spreadsheet(data):
    spreadsheet = get_spreadsheet()
    worksheet = spreadsheet.get_worksheet(0)
    worksheet.append_row(data)