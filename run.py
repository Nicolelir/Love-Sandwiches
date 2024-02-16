# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [ #The scope lists the APIs that the  program should access in order to run.
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json') #we call the from_service_account_file  method of the Credentials class, and we pass it our creds.json file name.
SCOPED_CREDS = CREDS.with_scopes(SCOPE) # Using the  with_scopes method of the creds object, and pass it our scope variable.
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS) # Using the gspread authorize method,  and pass it our SCOPED_CREDS.
SHEET = GSPREAD_CLIENT.open('love_sandwiches') # we can access our  love_sandwiches sheet, using the open() method on our client object  and passing it the name we gave our spreadsheet.

sales = SHEET.worksheet('sales') #define a new variable named “sales” and using the worksheet method of the sheet,  we can call our “sales” worksheet.  

data = sales.get_all_values() #we’ll use the gspread method get_all_values() to pull all the values from our sales worksheet.  

print(data)