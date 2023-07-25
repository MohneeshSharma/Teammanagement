#import sys
#import os

# Add the path to the Teammanagement folder to the Python path
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#import gspread
#from oauth2client.service_account import ServiceAccountCredentials

#scope = ['https://www.googleapis.com/auth/spreadsheets',
#         'https://www.googleapis.com/auth/drive']


#credentials = ServiceAccountCredentials.from_json_keyfile_name('keyfile.json', scope)
#client = gspread.authorize(credentials)

#spreadsheet = client.open('DataSheet') #change
#worksheet = spreadsheet.worksheet('Sheet1') #this is to work on a specific sheet

#print('------------------>connected to database<----------------------')

# TODO create add_user function (adds user to spreadsheet given name and serial numbers)
# TODO create remove_user function (removes user from spreadsheet given name and serial name)

from flask import Flask, request, jsonify
from flask_cors import CORS
from parent_folder.module.spreadsheet_utils import add_data_to_spreadsheet
from parent_folder.add_user import add_user

app = Flask(__name__)
CORS(app)



@app.route('/add_user', methods=['POST'])
def add_user_route():
    return add_user()


# other code goes here

if __name__ == '__main__':
    app.run()

# TODO fix backend error 'POST http://localhost:5500/add_user 405 (Method Not Allowed)'
# TODO fix error Error: SyntaxError: Unexpected end of JSON input