# Functions for reading tables and databases

import glob
from database import *


# YOU DON'T NEED TO KEEP THE FOLLOWING CODE IN YOUR OWN SUBMISSION
# IT IS JUST HERE TO DEMONSTRATE HOW THE glob CLASS WORKS. IN FACT
# YOU SHOULD DELETE THE PRINT STATEMENT BEFORE SUBMITTING

# Write the read_table and read_database functions below

def read_table(filename):
    '''(str) -> dict

    The function creates a Table object by obtaining information by a filename.
    It then processes the information and adds it to the Table object.

    REQ: The filename has to be exactly as the name of the file.
    REQ: The file must exist and be in the same directory.

    >>>a = read_table('movies.csv')
    >>>a.print_csv()
    >>>a.print_csv()
    m.studio,m.title,m.year,m.gross
    Par.,Titanic,1997,2186.8
    NL,The Lord of the Rings: The Return of the King,2003,1119.9
    BV,Toy Story 3,2010,1063.2
    '''
    # creates a new Table
    table = Table()

    # open file indicated with the given name
    filehandle = open(filename, 'r')

    # reads the first line
    first_line = filehandle.readline()

    # removes the new line at the end of the string
    strip = first_line.strip('\n')

    # splits the headers where ever there is a ','
    headers = strip.split(',')

    # list that will contain the elements of each line
    list_element = []

    # read the other lines and create a list, each element being one line
    lines = filehandle.readlines()

    # loop through each line
    for line in lines:

        # strip new line from the end of each string
        stripped_newline = line.strip('\n')

        # if there is no '\n', the continue
        if not line.strip():
            continue

        # split each line with ','
        each_line = stripped_newline.split(',')

        # this is a new list that will contain the elements with the space
        # stripped at the beginning of it
        stripped_space = []

        # loop through each element in each_line
        for element in each_line:

            # strip any trailing white space of each element
            strip_space = element.lstrip()

            # add it to the list called stripped_space
            stripped_space.append(strip_space)

        # adds stripped_space to list_element
        list_element.append(stripped_space)

    for i in range(0, len(headers), 1):
        # list that will contain the column
        column = []

        # loop as many times as the length of the header
        for a in range(0, len(list_element), 1):
            column.append(list_element[a][i])

        # applies add_columns() method to the Table
        table.add_columns(headers[i], column)

    # closes file
    filehandle.close()

    # returns the table
    return table


def read_database():
    '''NoneType -> Database

    The function creates a Database object by obtaining all the files in the
    directory with '.csv' and proccessing them through the read_table()
    function. Afterwards, it adds them into the Database object.

    REQ: Files for the Database must be in the same directory.

    >>>a = read_database()
    <database.Database object at 0x03A90850>
    '''
    # new Database object
    database = Database()

    # looks for files in the directory with '.csv' and inputs them into a list
    # with each element being there names
    file_list = glob.glob('*.csv')

    # dictionary that will be used create the database object
    database_dict = {}

    # list that will have the table names
    table_name = []

    # the list that will hold the table objects
    table_obj = []

    # loops through the list with all the file_names in the directory
    # with '.csv'
    for file in file_list:

        # finds the position of '.'
        name = file.replace('.csv', '')

        # adds the name to the table_name list
        table_obj = read_table(file)

        # adds tables to the Database
        database.add_tables(name, table_obj)

    # returns the Database object
    return database