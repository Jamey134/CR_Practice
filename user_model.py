# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Users:
    DB = "users_schema.users" # <--- double-check
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = """
        
        INSERT INTO users_schema.users (first_name, last_name, email)
        VALUES (%(first_name)s,%(last_name)s,%(email)s);
        
        """
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append(cls(user) )
        return users
            



