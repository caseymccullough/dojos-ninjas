from ..config.MySQLConnection import connectToMySQL

class Ninja:
   def __init__(self,data):
      self.id = data['id']
      self.first_name= data['first_name']
      self.last_name = data['last_name']
      self.age = data['age']
      self.dojo_id = data['dojo_id']
      self.updated_at = data['updated_at']
      

   def __str__(self) -> str:
      return "" + self.first_name, self.last_name

   @classmethod
   def get_all(cls):
      query = """SELECT ninjas.first_name, ninjas.last_name, ninjas.age, ninjas.dojo_id, dojos.name AS 'dojo' 
                  FROM ninjas
                  INNER JOIN dojos ON ninjas.dojo_id = dojos.id;
               """
      ninjas_from_db =  connectToMySQL('dojos_and_ninjas').query_db(query)
      ninjas =[]
      for n in ninjas_from_db:     
         ninjas.append(n)

      return ninjas

   @classmethod
   def get_dojo_ninjas(cls, data):
      query = """ SELECT ninjas.first_name, ninjas.last_name, ninjas.age
                  FROM ninjas
                  WHERE ninjas.dojo_id = %(id)s;
               """
      ninjas_from_db =  connectToMySQL('dojos_and_ninjas').query_db(query, data)
      ninjas = []
      for n in ninjas_from_db:     
         ninjas.append(n)
      print ("ninjas in dojo:", ninjas)
      return ninjas
      
   @classmethod
   def save(cls, data):
      query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id, updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW());"
      return connectToMySQL('dojos_and_ninjas').query_db(query, data)