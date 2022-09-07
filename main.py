from classes import Pessoa
from dataset.livros import dataset
from db.database import Database
from helper.WriteAJson import writeAJson

db=Database(database="livros", collection="livros",dataset=dataset)
db.resetDatabase()
pessoa = Pessoa()
pessoa.db = db

pessoa.create_livro(3, "O Senhor dos Anéis: A Sociedade do Anel ", "J.R.R. Tolkien", 2019, 39.9)
pessoa.create_livro(4, "Fogo & Sangue – Volume 1", "George R. R. Martin", 2018, 68.94)
pessoa.create_livro(5, "Admirável mundo novo", " Aldous Leonard Huxley", 2014, 28.79)

#Atualizando os dados do livro 2
pessoa.update_preco(2,56.90)
#Vou deletar o livro 3 só para teste

pessoa.delete_livro(3)

livros=pessoa.read_all()
writeAJson(livros,"Todos os livros")