class ControleRemoto():
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def passar_canal(self, botao):
        if botao == "+":
            print("Canal aumentado")
        elif botao == "-":
            print("Canal diminuído")
            
controle_remoto = ControleRemoto("preto", "10cm", "2cm", "2cm")
controle_remoto.passar_canal("+")

controle_remoto2 = ControleRemoto("branco", "10cm", "2cm", "2cm")     
controle_remoto2.passar_canal("-")
