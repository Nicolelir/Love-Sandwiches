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

    #--3-- while true our input request and data validation  is repeated each time the loop runs. 
    while True: 
        print("Please enter sales data from the last market.") #First, we need to instruct our user  to provide us with their sales data.  
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n") #a backslash and the letter n, is for an extra line of space under the example data

        data_str = input("Enter your data here: ") #Next, let’s use the input() method to get our sales  data from the user in the terminal.
    # print(f"The data provided is {data_str}") just for checking the code works, after that we can delete it. 
    
    #VALIDATION--In order to check that the data is valid,  
    #we need to convert our string value into a list  of values. Each value is separated by a comma.
    #So, we’ll define a new variable called sales_data: 
    
        sales_data = data_str.split(",") #use the split() method on our data  string, to break it up at the commas, This will remove the commas from the string.
    # each value from  our string has been added to the list, the commas here separate the items in the list, they are not the same string commas  that we removed with the split method.  
    
        if validate_data(sales_data):  #--3-- if statement is True or False. The break keyword, will end our while loop.  
            print("Data is valid!") #--3-- set a condition to  end our while loop. 
            break  #--3-- 
 
    return sales_data  #--3-- return our validated  sales_data from the get_sales_data function.  

#create a function to validate our data before allowing the rest of the program to continue.   
def validate_data(values): #And we will pass it a parameter  of “values” which will be our sales data list.
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """

    try:
        [int(value) for value in values] # --2-- tried this first in shell and it worked so we added after created try and except
        if len(values) != 6: #The len() method returns the length of  the list - the number of values in it.  
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e: #we're assigning that ValueError object to the e variable, which is standard Python shorthand for “error”.
        print(f"Invalid data: {e}, please try again.\n")
        return False  #--3-- If an error is thrown inside our except statement,  we can return False from the programme instead.

    return True  #--3--  If our function runs without any errors, we can return True after the try except statement has completed.

data = get_sales_data()#call the function It’s python3 run.py in console
                       # we add data = in --3-- so  Now our function returns a  value, we need a place to put it, back where it was called. So let’s  define a new variable here called data.
