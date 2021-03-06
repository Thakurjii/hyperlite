"""   It's all about processes and tasks. 

    --------------------
    Classes :
        
        -----------------
        * Process
        -----------------

    --------------------
"""

from .request_parser import ParsedData
from .collection import Collection
from .collection import Collections
from .database import Databases
from hyperql import parser


class Process(object):
    """     
        This class creates an executable process for every task.    

        Takes ParsedData() as parameter and executes the operations
        on ParsedData() as per it's Request Type.
    """

    def __init__(self, process_data: ParsedData):
        self.process_data: ParsedData = process_data

    def exec(self):
        """
            Instance method to execute Process().

            exec method executes the task associated with the Process.
            It resolves the tasks on the basis of the RequestType of the ParsedData().
        """

        # If the RequestType is Read
        if self.process_data.request_type == 'Read':

            # Retrieve db_name, col_name and HyperQL query
            # from the process_data
            db_name, col_name, query = Collection.meta_separator(self.process_data.meta_data)

            # get Database object and Collection object
            # on which operation is to be performed
            db = Databases.get_db(db_name)
            col = Collections.get_collection(col_name)

            # get Query() object from HyperQL query
            # Query() contains required_field and needed_query_methods
            query_object = parser.hyperql_parser(query)

            echo_queries = [] # stores echo query instructions

            # If the Collection object belongs to Database db
            if col.parent is db:
                
                # The HyperQl query is parsed with bottom-up approach,
                #   filtered_data stores the remaining data after every iteration of query parsing.
                filtered_data = None

                # Iteration on needed_query_methods with bottom-up approach.
                # instruction is a dict() object which contains field, data
                # (on which operation is to be performed) and 
                # required filter i.e. required method for Query Operation
                for instruction in query_object.needed_query_methods[::-1]:
                    
                    # if the instruction doesn't contain echo Operation
                    if instruction['filter'] is not parser.QueryOperations.echo:

                        # For first iteration
                        if filtered_data is None:

                            # Store retrieved data as filtered_data
                            filtered_data = col.read(objects=col.objects, instruction=instruction)
                        
                        # If filtered_data is not None
                        else:

                            # Replace filtered_data with new retrieved data
                            filtered_data = col.read(objects=filtered_data, instruction=instruction)
                    
                    # If the instruction contains echo Operation
                    else:

                        # Store all echo Operations in echo_queries
                        echo_queries.append(instruction)
                
                # Perform all echo operations together and return required data.
                return col.read(objects=filtered_data, instructions=echo_queries)

        # If the RequestType is Insert
        elif self.process_data.request_type == 'Insert':

            # Retrieve db_name, col_name from the process_data
            db_name, col_name = Collection.meta_separator(self.process_data.meta_data)

            # get Database object and Collection object
            # on which operation is to be performed
            db = Databases.get_db(db_name)
            col = Collections.get_collection(col_name)

            # If the Collection object belongs to Database db
            if col.parent is db:

                # Insert user_data as new Object in specified Collection
                # and return object id as acknowledgement.
                return col.insert(self.process_data.user_data)
            
        # If the RequestType is Delete
        elif self.process_data.request_type == 'Delete':

            # Retrieve db_name, col_name and object_id from the process_data
            db_name, col_name, object_id = Collection.meta_separator(self.process_data.meta_data)

            # get Database object and Collection object
            # on which operation is to be performed
            db = Databases.get_db(db_name)
            col = Collections.get_collection(col_name)

            # If the Collection object belongs to Database db
            if col.parent is db:
                
                # returns True if the object is removed
                return col.delete(object_id)
        
        # If the RequestType is Update
        elif self.process_data.request_type == 'Update':
            
            # Retrieve db_name, col_name and object_id from the process_data
            db_name, col_name, object_id = Collection.meta_separator(self.process_data.meta_data)

            # get Database object and Collection object
            # on which operation is to be performed
            db = Databases.get_db(db_name)
            col = Collections.get_collection(col_name)

            # If the Collection object belongs to Database db
            if col.parent is db:
                
                # returns True if the object is updated
                return col.update(object_id)

        raise Exception
