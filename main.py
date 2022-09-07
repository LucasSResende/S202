from dataset.cliente import dataset
from db.database import Database
from helper.WriteAJson import writeAJson

db=Database(database="database", collection="cliente", dataset=dataset)


livros = db.create(1, "O Senhor dos Anéis: A Sociedade do Anel ", "J.R.R. Tolkien", 2019, 39.9)
livros = db.create(2, "Fogo & Sangue – Volume 1", "George R. R. Martin", 2018, 68.94)
livros = db.create(3, "Admirável mundo novo", " Aldous Leonard Huxley", 2014, 28.79)

#Atualizando os dados do livro 2
livros=db.update(2,(56.90))
#Vou deletar o livro 3 só para teste

livros=db.delete(3)

livros=db.read()
writeAJson(livros,"Todos os livros")