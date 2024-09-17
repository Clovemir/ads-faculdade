class Livro:
    def __init__(self, titulo, autor, isbn, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro ' {self.titulo}' foi emprestado")
        else:
            print(f"O livro' {self.titulo}' Não está disponível para empréstimo.")
    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro'{self.titulo}' Foi devolvidoo.")
        else:
            print(f"O livro'{self.titulo}' ja esta disponível.")
    def exibir_info(self):
        status = "disponivel" if self.disponivel else "indisponivel"
        print(f"Título:{self.titulo}\nAutor:{self.autor}\nDisponibilidade: {status}")

livro1 = Livro ("Como convencer alguem em 90 segundos", "autor de gestao","12412412",2002)
livro2 = Livro ("jornada Python", "Autor de tecnologia","2389323", 2002)
livro1.exibir_info()
livro1.emprestar()
livro1.exibir_info()
livro1.devolver()
livro1.exibir_info()
