from reading import *
from database import *


# Below, write:
# *The cartesian_product function

def cartesian_product(table1, table2):
    '''(Table, Table) -> Table

    The function takes two Tables and pairs each row in Table1 with a row in
    in Table 2 and creates a whole new table out of it.

    REQ: The Table Objects must be populated with a data (Cannot be empty).

    >>>a = read_table('movies.csv')
    >>>b = read_table('oscars.csv')
    >>>c = cartesian_product(a, b)
    >>>c.print_csv()
    o.year,o.title,m.year,m.studio,m.title,m.gross,o.category
    2010,Toy Story 3,1997,Par.,Titanic,2186.8,Animated Feature Film
    2003,The Lord of the Rings: The Return of the King,1997,Par.,Titanic, \n
    2186.8,Directing
    1997,Titanic,1997,Par.,Titanic,2186.8,Directing
    1997,Titanic,1997,Par.,Titanic,2186.8,Best Picture
    2010,Toy Story 3,2003,NL,The Lord of the Rings: The Return of the King, \n
    1119.9,Animated Feature Film
    2003,The Lord of the Rings: The Return of the King,2003,NL,The Lord of \n
    the Rings: The Return of the King,1119.9,Directing
    1997,Titanic,2003,NL,The Lord of the Rings: The Return of the King, \n
    1119.9,Directing
    1997,Titanic,2003,NL,The Lord of the Rings: The Return of the King, \n
    1119.9,Best Picture
    2010,Toy Story 3,2010,BV,Toy Story 3,1063.2,Animated Feature Film
    2003,The Lord of the Rings: The Return of the King,2010,BV,Toy \n
    Story 3,1063.2,Directing
    1997,Titanic,2010,BV,Toy Story 3,1063.2,Directing
    1997,Titanic,2010,BV,Toy Story 3,1063.2,Best Picture
    '''
    # creates a new table
    new_table = Table()

    # finds the names of columns in table1
    column_names1 = table1.column_names()

    # finds the names of the columns in table2
    column_names2 = table2.column_names()

    # a list that contains the name of all the headers
    headers = column_names1 + column_names2

    # get the rows in table1
    rows1 = table1.get_rows()

    # get the rows in table2
    rows2 = table2.get_rows()

    # number of rows in table1
    num_rows1 = table1.num_rows()

    # number of rows in table2
    num_rows2 = table2.num_rows()

    # creates a munipulated list of rows1
    new_column = table1_columns_multiply(rows1, num_rows2)

    # creates a manipulated list of rows2
    new_column2 = table2_columns_multiply(rows2, num_rows1)

    # loops through each element in new_column2 and adds it to the list
    # new_column
    for i in new_column2:
        new_column.append(i)

    # loops as many times as the length of headers
    for i in range(0, len(headers), 1):

        # creats a variable column for each list element in new_column
        column = new_column[i]

        # runs the add columns method for new_table object
        new_table.add_columns(headers[i], column)

    # returns the final table object
    return new_table


# *All other functions and helper functions

def table1_columns_multiply(rows1, num_rows2):
    '''(list of lists, int) -> list of lists

    The function takes a list of lists and multiplies each element in the list
    by the int given by num_rows1 and outputs the new list.

    REQ: num_rows1 >= 0

    >>>rows1 = ['d','a','b']
    >>>num_rows1 = 2
    >>>table2_columns_multiply(rows2, num_rows1)
    ['d', 'd', 'a', 'a', 'b', 'b']
    >>>rows2 = []
    >>>num_rows1 = 4
    >>>table2_columns_multiply(rows2, num_rows1)
    []
    >>>rows2 = ['f']
    >>>num_rows1 = 6
    >>>table2_columns_multiply(rows2, num_rows1)
    ['f','f','f','f','f','f']
    >>>rows2 = ['f,d,d,d']
    >>>num_rows1 = 3
    >>>table2_columns_multiply(rows2, num_rows1)
    ['f,d,d,d','f,d,d,d','f,d,d,d']
    '''
    # a list that will contain the manipulated rows in table1
    new_column = []

    # loops through each element in rows1
    for i in rows1:

        # will contain the values of the manipulated column
        new_column1 = []

        # adds each column to new_row1
        new_column.append(new_column1)

        # loops through each element in the list that is within rows1
        for a in i:

            # adds each element to new_colum1 as many times as the number
            # of rows in rows2
            for f in range(0, num_rows2, 1):

                # adds each element to new_column1
                new_column1.append(a)

    # returns new_column
    return new_column


def table2_columns_multiply(rows2, num_rows1):
    '''(list of lists, int) -> list of lists

    The function takes a list of lists and multiplies them by the int given
    by num_rows1. Some confusion can arise as to how they are multiplied, so
    that it is clear, the lists are multiplied. This means if you had a list
    of [1,2,3] and wanted to multiply it 3 times, it will result with
    [1,2,3,1,2,3,1,2,3].

    REQ: num_rows1 >= 0

    >>>rows2 = ['d','a','b']
    >>>num_rows1 = 2
    >>>table2_columns_multiply(rows2, num_rows1)
    ['d','a','b','d','a','b']
    >>>rows2 = []
    >>>num_rows1 = 4
    >>>table2_columns_multiply(rows2, num_rows1)
    []
    >>>rows2 = ['f']
    >>>num_rows1 = 6
    >>>table2_columns_multiply(rows2, num_rows1)
    ['f','f','f','f','f','f']
    >>>rows2 = ['f,d,d,d']
    >>>num_rows1 = 3
    >>>table2_columns_multiply(rows2, num_rows1)
    ['f,d,d,d','f,d,d,d','f,d,d,d']
    '''
    # new list that will contain all the modified table columns
    new_column2 = []

    # loops through each element in rows2
    for a in rows2:

        # creates a new list that will contain the modified column
        column_manipulate = []

        # adds the list containing the modified column into new_column2
        new_column2.append(column_manipulate)

        # loops as many times as the number of rows in table1
        for i in range(0, num_rows1, 1):

            # adds each element in rows2 into column_manipulate
            column_manipulate.extend(a)

    # returns the new list containing all the modified table columns
    return new_column2


def multiple_tables(table_obj_list, base_table):
    '''(list of Tables, Table) -> Table

    The function takes in a list of Tables and a base table. If the list has
    more than one Table in it, it would apply the cartesian_product() function
    until only one Table remains. It returns that new Table.

    REQ: The Tables should not be empty.

    >>>a = read_table('movies.csv')
    >>>b = read_table('oscars.csv')
    >>>c = [a, b]
    >>>d = read_table('books.csv')
    >>>e = multiple_tables(c, d)
    >>>e.print_csv()
    book.title,book.author,o.year,o.title,o.category,book.year
    Godel Escher Bach,Douglas Hofstadter,2010,Toy Story 3,Animated \n
    Feature Film,1979
    Godel Escher Bach,Douglas Hofstadter,2003,The Lord of the Rings: \n
    The Return of the King,Directing,1979
    Godel Escher Bach,Douglas Hofstadter,1997,Titanic,Directing,1979
    Godel Escher Bach,Douglas Hofstadter,1997,Titanic,Best Picture,1979
    What if?,Randall Munroe,2010,Toy Story 3,Animated Feature Film,2014
    What if?,Randall Munroe,2003,The Lord of the Rings: The Return of the \n
    King,Directing,2014
    What if?,Randall Munroe,1997,Titanic,Directing,2014
    What if?,Randall Munroe,1997,Titanic,Best Picture,2014
    Thing Explainer,Randall Munroe,2010,Toy Story 3,Animated Feature Film,2015
    Thing Explainer,Randall Munroe,2003,The Lord of the Rings: The Return of \n
    the King,Directing,2015
    Thing Explainer,Randall Munroe,1997,Titanic,Directing,2015
    Thing Explainer,Randall Munroe,1997,Titanic,Best Picture,2015
    Alan Turing: The Enigma,Andrew Hodges,2010,Toy Story 3,Animated Feature \n
    Film,2014
    Alan Turing: The Enigma,Andrew Hodges,2003,The Lord of the Rings: The \n
    Return of the King,Directing,2014
    Alan Turing: The Enigma,Andrew Hodges,1997,Titanic,Directing,2014
    Alan Turing: The Enigma,Andrew Hodges,1997,Titanic,Best Picture,2014
    '''
    # if table_obj_list has more than one element in it
    if len(table_obj_list) > 1:

        # call base_table as t2
        t2 = base_table

        # sets an index
        i = 1

        # loops through each element element in table_obj_list with the
        while i < len(table_obj_list):

            # passes t2 and the next element after it into the
            # cartesian_product() function
            t2 = cartesian_product(t2, table_obj_list[i])

            # every itteration increases index by 1
            i += 1

    # else if it has 1
    else:

        # t2 is base_table
        t2 = base_table

    # returns variable t2
    return t2


def contraints_operator(constraints, t2):
    '''(list of str, Table) -> Table

    The function takes the the string after where clause and applies the
    modifications of the constraints to the Table.

    REQ: Each element in constraints contains either '=' or '>'.
    REQ: Element before the constraints('=' or '>') are columns.
    REQ: Elements after the constraints('=' or '>') are either columns or
    srtrings or ints.

    >>>a = read_table('movies.csv')
    >>>b = ['m.title>yolo']
    >>>c = contraints_operator(b, a)
    >>>c.print_csv()
    m.gross,m.year,m.title,m.studio
    2186.8,1997,Titanic,Par.
    1119.9,2003,The Lord of the Rings: The Return of the King,NL
    1063.2,2010,Toy Story 3,BV
    '''
    # sets an initial operator
    operator = ''

    # loops through the constraints
    for i in constraints:

        # loops through as many times as the length of elements in list
        # constraints
        for a in range(0, len(i), 1):

            # sets an initial index
            index = 0

            # while looping, if it finds '='
            if i[a] == '=':

                # sets the index as the point at where it finds '='
                index = a

                # sets the operator as '='
                operator = '='

                # slices the list, everything up until the operator
                column1 = i[:index]

                # slices the list, everything after the operator
                column2 = i[index + 1:]

            # while looping, if it finds '>'
            elif i[a] == '>':

                # sets the index as the point at where it finds '>'
                index = a

                # sets the operator as '>'
                operator = '>'

                # slices the list, everything up until the operator
                column1 = i[:index]

                # slices the list, everything after the operator
                column2 = i[index + 1:]

        # applies the constraint_operating() method to the Table
        t2.constraint_operating(column1, column2, operator)

    # returns the modified Table
    return t2


def get_columns_selected(selected_columns, t2):
    '''(list of str, Table) -> Table

    The function creates a new table with only the selected columns from the
    original Table.

    REQ: Elements in selected_columns must exist in t2.

    >>>a = read_table('movies.csv')
    >>>b = ['m.year']
    >>>c = get_columns_selected(b, a)
    >>>c.print_csv()
    m.year
    1997
    2003
    2010
    '''
    # the gets those columns given columns
    columns = t2.get_selected_columns(selected_columns)

    # new table that will have all selected columns
    new_table = Table()

    # loops as many times as the length of selected_columns
    for i in range(0, len(selected_columns), 1):

        # headers will be each element in selected_columns
        headers = selected_columns[i]

        # column will be each column in columns
        column = columns[i]

        # will apply the add_columns method to the new_table
        new_table.add_columns(headers, column)

    # returns the new_table
    return new_table


# *Main code that obtains queries from the keyboard,
# processes them, and uses the below function to output csv results

def run_query(database, query):
    '''(Database, str) -> Table

    The function takes a query and Database where it makes a Table, applies
    the constraints, applies the cartesian product, applies the selected
    columns and makes a whole new Table.

    REQ: Database must consist for files.
    REQ: Query must be given in the specific format:
         select ____ from ____ where ____

    >>>database = read_database()
    >>>query = 'select m.title,m.studio,m.gross,o.category from movies, \n
    oscars where m.title=o.title'
    >>>a = run_query(database, query)
    >>>a.print_csv()
    o.category,m.studio,m.gross,m.title
    Directing,Par.,2186.8,Titanic
    Best Picture,Par.,2186.8,Titanic
    Directing,NL,1119.9,The Lord of the Rings: The Return of the King
    Animated Feature Film,BV,1063.2,Toy Story 3
    '''

    # splits the query where there is a space and adds each element to a list
    tokens = query.split()

    # finds the index of the string 'from' in the list
    index = tokens.index('from')

    # finds the index of the string 'where' in the list
    index2 = tokens.index('where')

    # slices the list to form a new smaller list such that everything a after
    # 'from' is part of the new list

    table_keys = tokens[index + 1].split(',')
    # a list that will contain all the Table Objects

    table_obj_list = []
    # loops through the list table_keys

    for tables in table_keys:

        # for each element in table_keys is used as the key to get the Table
        # Object from Database Object
        table_obj = database.get_tables(tables)

        # adds each Table Object to the list table_obj_list
        table_obj_list.append(table_obj)

    # the first element in table_obj_list is called the base_table
    base_table = table_obj_list[0]

    # function that primarily works for functioning when user inputs more than
    # one table
    t2 = multiple_tables(table_obj_list, base_table)

    # list that will contain the elements for the constraints
    constraints = tokens[index2 + 1].split(',')

    # function that primarily works for operating with constraints
    t2_constraints = contraints_operator(constraints, t2)

    # gets the list of columns to be selected
    selected_columns = tokens[1].split(',')

    # for the selected_columns, applies get_columns_selected() function
    new_table = get_columns_selected(selected_columns, t2_constraints)

    # returns the new, modified Table
    return new_table


if __name__ == '__main__':

    # gets a query
    query = input('Enter a SQuEaL query, or a blank line to exit:')

    # exit is False
    exit = False

    # while is is False
    while(exit is False):

        # if query is blank line
        if(query == ''):

            # exit is True
            exit = True

        # else if it is not a blank line
        else:

            # creates a Database
            database = read_database()

            # applies run_query() function
            new_table = run_query(database, query)

            # applies print_csv() method
            new_table.print_csv()

            # exit is True
            exit = True