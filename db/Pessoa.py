from db.database import Database
from pprint import pprint as pp
from bson.objectid import ObjectId

class PessoaDAO:
    def __int__(self):
        self.db = Database(database="cliente", collection="Pessoa")
        self.collection = self.db.collection

    def create_pessoa(self, nome:str, idade: int):
        res = self.collection.insert_one({"nome": nome, "idade": idade})
        return res.inserted_id

    def read_pessoa_by_id(self, id: str):
        res = self.collection.find_one({"id": ObjectId(id)})
        return res

    def read_all(self):
        res = self.collection.find()
        return res

    def update_pessoa(self, id: str, nome: str, idade: int):
        res = self.collection.update_one({"_id":ObjectId(id)},{"$set": {"nome":nome, "idade": idade}})
        return res.modified_count

    def delete_pessoa(self, id: str):
        res = self.collection.delete_one({"_id": ObjectId(id)})
        return res.deleted_count
