class Table():
    '''A class to represent a SQuEaL table'''

    def __init__(self):
        '''() -> Nonetype

        Runs and creates an empty dictionary as the Table is made.
        '''
        # creates an empty dictionary
        self._new_dict = {}

    def num_rows(self):
        '''() -> int

        The method the amount of rows that the dictionary currently holds.
        '''
        # finds the keys in the dictionary
        header = list(self._new_dict.keys())

        # if there are no headers
        if(len(header) == 0):

            # the number of rows is 0
            rows = 0

        # else if there are headers
        else:

            # the number of rows is the number of elements in the column list
            # at mapped with the first element in the header list
            rows = len(self._new_dict[header[0]])

        # returns the length of the list that the key is holding
        return rows

    def add_columns(self, headers, column):
        '''(str, list of str) -> NoneType

        The method adds columns with the given list and the given header as the
        key.
        '''
        # adds the list to the dictionary with the header name
        self._new_dict[headers] = column

    def constraint_operating(self, column1_header, cond2, operator):
        '''() -> NoneType

        The method applies the constraints to the column.
        '''
        # gets the column from the dictionary
        column1 = self._new_dict[column1_header]

        # a list that will contain all the items that need to be removed
        remove_list = []

        # if the operator is '='
        if(operator == '='):

            # if its a string
            if (cond2[0] == "'" and cond2[-1] == "'"):

                # take the quotation marks out
                strip_quotes = cond2[1:len(cond2)-1]

                # loop as many times as length of column1
                for i in range(0, len(column1)):

                    # if the elements in the column1 do not equal strip_quotes
                    if (column1[i] != strip_quotes):

                        # add it to the list to be removed
                        remove_list.append(i)

            # else if cond2 is not a string
            else:
                # get column from the dictionary
                column2 = self._new_dict[cond2]

                # loop as many times as the length of column1
                for i in range(0, len(column1)):

                    # if the element in column1 is not in column2
                    if (column1[i] != column2[i]):

                        # add it to the list of elements that will be removed
                        remove_list.append(i)

            # if the operator is '>'
            if(operator == '>'):

                # if it is a string
                if (cond2[0] == "'" and cond2[-1] == "'"):

                    # take the quotation marks out
                    strip_quotes = cond2[1:len(cond2)-1]

                    # loop as many times as length of column1
                    for i in range(0, len(column1)):

                        # tries a float value of elements in column1 and
                        # strip_quotes
                        try:
                            value1 = float(column1[i])
                            value2 = float(strip_quotes)

                        # if it is not a float value, use the value types that
                        # are given
                        except:
                            value1 = column1[i]
                            value2 = strip_quotes

                        # if the value of value1 is less than or equal to
                        # value2
                        if (value1 <= value2):

                            # add it to list that contains elements to be
                            # removed
                            remove_list.append(i)

                # else if cond2 is neither those, it is a column
                else:

                    # get column from the dictionary
                    column2 = self._new_dict[cond2]

                    # loop as many times as length of column1
                    for i in range(0, len(column1)):

                        # tries a float value of elements in column1 and
                        # column2
                        try:
                            value1 = float(column1[i])
                            value2 = float(column2[i])

                        # if it is not a float value, use the value types that
                        # are given
                        except:
                            value1 = column1[i]
                            value2 = column2[i]

                        # if value1 is not equal to value2
                        if (value1 != value2):

                            # add it to list that contains elements to be
                            # removed
                            remove_list.append(i)

        # check elements in remove_list and remove the elements from
        # the dictionary
        self.remove_rows(remove_list)

    def remove_rows(self, remove_list):
        '''(list of str) -> NoneType

        The method removes rows by checking the elements in remove_list.
        '''
        # gets the names of the columns
        keys = self.get_columns()

        # loop as many times as the length of remove_list
        for i in range(len(remove_list)-1, -1, -1):

            # for every element in keys
            for a in keys:

                # remove the row that should be removed
                self._new_dict[a].pop(remove_list[i])

    def get_columns(self):
        '''() -> list of str

        A simple method to get the name of columns
        '''
        # gets the names of the columns in the dictionary
        header = list(self._new_dict.keys())

        # returns the list with the names
        return header

    def get_selected_columns(self, headers):
        '''() -> list of lists

        A method that only gets the rows of the columns that it needs.
        '''
        # a list that will contain the elements of the selected_columns
        selected_rows = []

        # loop through each element in the header
        for i in headers:

            # add each row to the selected_rows list
            selected_rows.append(self._new_dict[i])

        # return the list with the selected_rows
        return selected_rows

    def get_rows(self):
        '''() -> list of lists

        The method simply gets all the columns with the row elements in it
        from the dictionary.
        '''
        # gets a list of all the keys in the dictionary
        header = list(self._new_dict.keys())

        # a list that will contain all columns with their row elements
        column = []

        # loops as many times as the length of headers
        for i in range(0, len(header), 1):

            # index is the element in the header
            index = header[i]

            # add the columns to the column list
            column.append(self._new_dict[index])

        # returns colum
        return column

    def column_names(self):
        '''() -> list of str

        A simple method that returns a list full of the keys in the dictionary.
        '''
        # returns a list with all the keys in the dictionary
        return list(self._new_dict.keys())

    def set_dict(self, new_dict):
        '''(Table, dict of {str: list of str}) -> NoneType

        Populate this table with the data in new_dict.
        The input dictionary must be of the form:
            column_name: list_of_values
        '''
        # adds the information of new_dict to the table
        self._new_dict = new_dict

    def get_dict(self):
        '''(Table) -> dict of {str: list of str}

        Return the dictionary representation of this table. The dictionary keys
        will be the column names, and the list will contain the values
        for that column.
        '''
        # returns the table as a dictionary
        return self._new_dict

    def print_csv(self):
        '''(Table) -> NoneType
        Print a representation of table in csv format.
        '''
        # no need to edit this one, but you may find it useful (you're welcome)
        dict_rep = self.get_dict()
        columns = list(dict_rep.keys())
        print(','.join(columns))
        rows = self.num_rows()
        for i in range(rows):
            cur_column = []
            for column in columns:
                cur_column.append(dict_rep[column][i])
            print(','.join(cur_column))


class Database():
    '''A class to represent a SQuEaL database'''

    def __init__(self):
        '''() -> NoneType

        Creates an empty dictionary when the Database is created.
        '''
        # create an empty dictionary
        self._new_dict = {}

    def get_tables(self, table_name):
        '''(str) -> Table

        Finds the Table object in the dictionary with the key given and
        returns it.
        '''
        return self._new_dict[table_name]

    def add_tables(self, name, table):
        '''(str, Table) -> NoneType

        The method adds a Table to the dictionary with the key being the name
        of it.
        '''
        self._new_dict[name] = table

    def set_dict(self, new_dict):
        '''(Database, dict of {str: Table}) -> NoneType

        Populate this database with the data in new_dict.
        new_dict must have the format:
            table_name: table
        '''
        # adds the tables of new_dict to the databse
        self._new_dict = new_dict

    def get_dict(self):
        '''(Database) -> dict of {str: Table}

        Return the dictionary representation of this database.
        The database keys will be the name of the table, and the value
        with be the table itself.
        '''
        # returns the database as a dictionary
        return self._new_dict