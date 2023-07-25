from flask import Flask, request, jsonify
#from modules.spreadsheet_utils.spreadsheet_utils import add_data_to_spreadsheet
#from backend.modules.spreadsheet_utils.spreadsheet_utils import add_data_to_spreadsheet
from module.spreadsheet_utils import add_data_to_spreadsheet



app = Flask(__name__)

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json # parse the JSON data from the request body

    # validation on the data goes here

    # add the data to google spreadsheet
    add_data_to_spreadsheet(data)

    # send response back to frontend
    response = {'message': 'User added successfully'}
    return jsonify(response)

if __name__ == '__main__':
    app.run()