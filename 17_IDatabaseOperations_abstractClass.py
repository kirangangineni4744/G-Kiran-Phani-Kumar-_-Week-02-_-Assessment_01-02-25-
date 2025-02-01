from abc import ABC,abstractmethod

class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def update(self): 
        pass

    @abstractmethod
    def delete(self):
        pass

class SQLDatabase(IDatabaseOperations):
    def insert(self): 
        print("Inserting into SQL Database")
    def update(self):
        print("Updating SQL Database")
    def delete(self):
        print("Deleting from SQL Database")

class NoSQLDatabase(IDatabaseOperations):
    def insert(self):
        print("Inserting into NoSQL Database")
    def update(self):
        print("Updating NoSQL Database")
    def delete(self):
        print("Deleting from NoSQL Database")

sql_db=SQLDatabase()
nosql_db=NoSQLDatabase()

sql_db.insert()
sql_db.update()
sql_db.delete()

nosql_db.insert()
nosql_db.update()
nosql_db.delete()
