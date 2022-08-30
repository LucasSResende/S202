from dataset import produto_database
from db.database import Database
from helper.WriteAJson import writeAJson
from dataset.pessoa_dataset import dataset as pessoa_dataset

pessoas = Database(
    database="database",
    collection="pessoas",
    dataset=pessoa_dataset
)
pessoas.resetDatabase()

produtos = Database(
    database="database",
    collection="produtos",
    dataset=produto_database
)
produtos.resetDatabase()


compra1 = produtos.collection.aggregate([
    {"$lookup":
        {
            "from": "pessoas",  # outra colecao
            "localField": "dono_id",  # chave estrangeira
            "foreignField": "_id",  # id da outra colecao
            "as": "dono"  # nome da saida
        }

     }
])



writeAJson(compra1, "compra1")

