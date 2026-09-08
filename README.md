# Aprendendo-POO
Eu aprendi POO Básica nesse projeto, Foi Bem no começinho da minha carreira...


# Irei explicar oque é POO...

POO significa Programação Orientada a Objetos.

Basicamente, é uma forma de organizar o código usando classes e objetos. A ideia é criar um modelo (classe) que tenha informações e ações, e depois criar objetos a partir desse modelo.

Por exemplo, podemos ter uma classe Pessoa. Ela pode ter informações como nome e idade, além de ações que uma pessoa pode realizar.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá! Meu nome é {self.nome} e tenho {self.idade} anos.")


pessoa = Pessoa("Cohla", 14)

pessoa.apresentar()

Nesse exemplo, Pessoa é a classe e pessoa é o objeto criado a partir dela.

O __init__ é usado para definir as informações iniciais do objeto, enquanto os métodos são funções que o objeto pode executar.

Estou estudando POO em Python e criei este projeto para praticar os conceitos básicos e entender melhor como classes e objetos funcionam na prática.
