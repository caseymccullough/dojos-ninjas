from ..config.MySQLConnection import connectToMySQL

class Dojo:
   def __init__(self,data):
      self.id = data['id']
      self.name= data['name']
      self.created_at = data['created_at']
      self.updated_at = data['updated_at']

   def __str__(self) -> str:
       return "" + self.name
   
   @classmethod
   def get_all(cls):
      query = "SELECT * FROM dojos;"
      dojos_from_db =  connectToMySQL('dojos_and_ninjas').query_db(query)
      dojos =[]
      for d in dojos_from_db:
         dojos.append(cls(d))
      return dojos
   
   @classmethod
   def get_by_id(cls, data):
      query = "SELECT * FROM dojos WHERE id = %(id)s;"
      # ninjas query to follow
      results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
      print (results) 
      dojo = cls(results[0])
      return dojo
   
   @classmethod
   def save(cls, data):
      query = "INSERT INTO dojos (name, created_at) VALUES (%(name)s, NOW());"
      return connectToMySQL('dojos_and_ninjas').query_db(query, data)