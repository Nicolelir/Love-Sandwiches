# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    Get sales figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
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


""" 
""" # in --9-- we dont use this 2 functions anymore, we change them for update_worksheet now.
#--5--build a  function that inserts this sales_data as a new entry in our sales  worksheet over in our Google Sheet.

####def update_sales_worksheet(data):
"""
Update sales worksheet, add new row with the list data provided
"""
#####print("Updating sales worksheet...\n") #--4--The purpose of this is to give the user some  feedback in the terminal as our program completes its task.
    
"""
Now we need to access our sales  worksheet from our Google Sheet  
so that we can add our data to it. So  we’ll declare a variable sales_worksheet,  
and then we use the sheet variable we defined at  the top of our page using the gspread library
"""
####sales_worksheet = SHEET.worksheet("sales") #--5-- And we’ll use the gspread worksheet()  method to access our sales worksheet.  
####sales_worksheet.append_row(data) #--5-- another of gspreads methods called append_row() and pass  it our data to be inserted. The append_row method adds a new row to the  end of our data in the worksheet selected. 
####print("Sales worksheet updated successfully.\n")

####def update_surplus_worksheet(data): # --8-- same as above, just change sales for surplus...
"""
Update surplus worksheet, add new row with the list data provided
"""
####print("Updating surplus worksheet...\n")
####surplus_worksheet = SHEET.worksheet("surplus")
####surplus_worksheet.append_row(data)
####print("Surplus worksheet updated successfully.\n")

"""
"""

def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet) # we'll use our worksheet variable here  to choose which worksheet we want to access.
    worksheet_to_update.append_row(data) # Now we can append our new row to our  worksheet_to_update.   
    print(f"{worksheet} worksheet updated successfully\n")


def calculate_surplus_data(sales_row): # --6-- Calculate surplus data..
    """
    Compare sales with stock and calculate the surplus for each item type.

    The surplus is defined as the sales figure subtracted from the stock:
    - Positive surplus indicates waste
    - Negative surplus indicates extra made when stock was sold out.
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values() #--6-- using the worksheet method of the sheet  variable again, we’ll let the sheet know that we want the data from the “stock” worksheet  this time.And we’ll use another method of the gspread library called get_all_values() to  fetch all of the cells from our stock worksheet.
    stock_row = stock[-1] #--6-- To make our surplus calculations, we need  to pull the last list out of our stock data.  List index of -1 will slice the final item from the list and return it to the new stock variable. 
   
  
    surplus_data = [] #--7-- access to 2 lists and iterate it at the same time...
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales #--7--convert the value at the same time as we access it. If we wrap this stock variable in the int() method it will return the converted integer,  and then we can subtract our sales value from it. 
        surplus_data.append(surplus)

    return surplus_data

def get_last_5_entries_sales(): #--10--get the last 5 records for each sandwhich
    """
    Collects columns of data from sales worksheet, collecting
    the last 5 entries for each sandwich and returns the data
    as a list of lists.
    """
    sales = SHEET.worksheet("sales")

    columns = [] # --10-- we want to get lists of numbers from every  column 1, 2, 3 and all the way up to column 6. we use a for loop....
    for ind in range(1, 7):
        column = sales.col_values(ind) # we’ll use the col_values() method on the  sales variable, and pass it our ind variable. 
        columns.append(column[-5:]) # we’ll append our column  list to our columns list. we want the last 5 items, so we can use -5 here inside our append method.

    return columns

def calculate_stock_data(data):#--11--we’ll pass it the stock_data that our get_last_5_entries_sales function returned.
    """
    Calculate the average stock for each item type, adding 10%
    """
    print("Calculating stock data...\n")
    new_stock_data = [] # our function needs to calculate the average from each list in our data. we use for loop....

    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column) / len(int_column)
        stock_num = average * 1.1 #add 10%
        new_stock_data.append(round(stock_num)) #we’ll append this calculated stock_num to the new_stock_data list outside the for loop.

    return new_stock_data # we can return the previuos values from our function  And assign it to a variable back where the function was called, we’ll call it stock_data.


def main(): # --6-- Calculate surplus...it's common practice to wrap the main function calls of a program within a function called main.
    """
    Run all program functions
    """
    data = get_sales_data()#call the function It’s python3 run.py in console
                       # we add data = in --3-- so  Now our function returns a  value, we need a place to put it, back where it was called. So let’s  define a new variable here called data.3
    sales_data = [int(num) for num in data] # --4--let’s create a new list comprehension here to transform strings into intergers. we’ll assign the result from the list  comprehension to a new variable named sales_data.
    ####update_sales_worksheet(sales_data)# --4--we dont need it in --9--
    update_worksheet(sales_data, "sales") #--9-- instead of update_sales_worksheet function, pass it that second value, for the worksheet parameter. “sales”.
    new_surplus_data = calculate_surplus_data(sales_data) #--6-- call the function from our main function and remember to pass it our sales data variable.
                                                        #--7-- new_surplus_data = is for the returned value (return surplus data above)
    ####update_surplus_worksheet(new_surplus_data)   #-- we dont need it it 9--      # --8-- to call my new function (update_surplus) and  make sure to pass it the data I want to insert.
    update_worksheet(new_surplus_data, "surplus") #--9--passing it the value of “surplus” as this time  we want to update the surplus worksheet. 
    sales_columns = get_last_5_entries_sales() #--11--
    stock_data = calculate_stock_data(sales_columns) #--11--return new_stock
    update_worksheet(stock_data, "stock") #--11--Now that we have our stock data calculated, all we need to do is insert our stock data into the stock worksheet.

print("Welcome to Love Sandwiches Data Automation")
main()

