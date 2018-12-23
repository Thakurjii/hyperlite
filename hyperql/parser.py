""" Parser module helps up to parse hyperql query language to an plan python object """

import re

class QueryOperations:
    @staticmethod
    def equal_to(data, field):
        return data == field

    @staticmethod
    def not_equal_to(data, field):
        return data != field

    @staticmethod
    def graeter_than(data, field):
        return data > field

    @staticmethod
    def less_than(data, field):
        return data < field

    @staticmethod
    def graeter_than_equal(data, field):
        return data >= field

    @staticmethod
    def less_than_equal(data, field):
        return data <= field

    @staticmethod
    def and_operation(data, field):
        return data and field

    @staticmethod
    def or_operation(data, field):
        return data or field

    @staticmethod
    def not_operation(field):
        return not field

class Query :
    def __init__(self):
        self.required_field = []
        self.needed_query_methods = {}

    

def hyperql_parser(query: str) -> Query:

    query_obj = Query()
    query_instractions = []

    # For removing the white spaces
    space_pattern = re.compile(r'\s+')
    
    def get_field_name(raw_query):
        return raw_query[0 : raw_query.find("=")]

    for instraction in query.split(","):
        query_instractions.append(re.sub(space_pattern, '', instraction))
    
    for raw_query in query_instractions:
        if raw_query.find("=") > -1:
            query_obj.required_field.append(get_field_name(raw_query))

    return query_obj



if __name__ == "__main__":
    query = """ 
            name = it, 
            age = it, 
            city &eq 'city_name'
            """
    obj = hyperql_parser(query)

    print(obj.required_field)