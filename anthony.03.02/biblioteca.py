class Pessoa:
    def __unit__(self,nome,numero,endereco):
        self.nome = nome
        self.numero = numero 
        self.endereco = endereco 
    
    def get_endereco(self):
        return self.endereco
    
    def atualizar_endereco(self, novo_endereco):
        self.endereco = novo_endereco 
    
    def get_numero(self):
        return self.numero 
    
    def atualizar_numero(self,novo_numero): 
        self.numero = novo_numero 
        
class Aluno(Pessoa):
    def __unit__(self , cod,curso ):
        self.cod = cod 
        self.curso = curso 
        
    def code_info(self):
        return self.cod 
    
    def curso_al(self):
        return self.curso
    if ():
        


class Funcionario(Pessoa):
    def __unit__(self,matricula,cargo,salario,disponivel):
        self.matricula = matricula 
        self.cargo = cargo
        self.salario = salario

        
        
class livro :
    def __unit__(self,titulo,autor,isbn,ano_publicado):
        self.titulo= titulo 
        self.autor=autor 
        self.isbn=isbn 
        self.ano= ano_publicado
        
        






class Biblioteca:
    def __unit__(self,nome_biblioteca,endereco_biblioteca,acervo_livros):