import pymongo

class MongoDBClient:
    def __init__(self, uri):
        self.uri = uri
    
    def connect(self):
        try:
            self.client = pymongo.MongoClient(self.uri)
            print("Conexión exitosa a MongoDB")
            return self.client
        except Exception as e:
            print("No se pudo establecer una conexión a MongoDB se recomineda restablecer su conexion ")
   
    
    def update_all_documents(self, db_name, coll_name, new_docs):
        try:
         db = self.client[db_name]
         coll = db[coll_name]
         
         coll.delete_many({})
         coll.insert_many(new_docs)
        except Exception as e:
         print("No se pudo establecer una conexión a MongoDB se recomineda restablecer su conexion ")
         
    def get_documents(self, db_name, coll_name, listap):
     db = self.client[db_name]
     coll = db[coll_name]
     docs = coll.find()
     for doc in docs:
      listap.append({"codigo":doc["codigo"],"nombre":doc["nombre"],"description":doc["description"],"precio":float(doc["precio"])})
      

