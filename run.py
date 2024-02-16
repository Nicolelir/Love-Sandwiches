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

def get_sales_data(): #add a docstring here to describe  what our get_sales_data function is going to do.
    """
    Get sales figures input from the user.
    """
    print("Please enter sales data from the last market.") #First, we need to instruct our user  to provide us with their sales data.  
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n") #a backslash and the letter n, is for an extra line of space under the example data

    data_str = input("Enter your data here: ") #Next, let’s use the input() method to get our sales  data from the user in the terminal.
    print(f"The data provided is {data_str}")


get_sales_data()#call the function It’s python3 run.py in console
