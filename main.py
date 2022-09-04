from db import database
from db.database import Database
from helper.WriteAJson import writeAJson

db = Database(database="database", collection="livros", dataset=database)


lvrs = db.create(1, "Como fazer amigos e influenciar pessoas ", "Dale Carnegie", 1936, 39.9)
lvrs = db.create(2, "A revolta de Atlas", "Ayn Rand", 1957, 71.91)
lvrs = db.create(3, "O caminho da servidão", "F.A Hayek", 1944, 46.95)

# Atualizando os dados do livro 2
lvrs = db.update(2, (56.90))
# Vou deletar o livro 3 só para teste

lvrs = db.delete(3)

lvrs = db.read()
writeAJson(lvrs, "Todos os livros")
