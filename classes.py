
class Pessoa():

    def __int__(self):
        pass

    def create_livro(self, id, titulo,autor,ano,preco):
        self.db.createbook(id, titulo,autor,ano,preco)

    def read_all(self):
        return self.db.readbook()


    def update_preco(self, id, preco):
        self.db.updateprice(id, preco)


    def delete_livro(self, id):
       self.db.deletebook(id)

