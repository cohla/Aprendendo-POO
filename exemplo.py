class Cliente:
        def __init__(self, nome, email, plano):
            self.nome = nome
            self.email = email
            self.lista_planos = ["Basic", "Premium"]    
            if plano in self.lista_planos:
                self.plano = plano
            else:
                 raise Exception("Plano inválido.")
        def mudar_plano(self, novo_plano):
            if novo_plano in self.lista_planos:
                 self.plano = novo_plano

            else:
                print("Plano inválido.")
                 

        def ver_filme(self, filme, plano_filme):
                if self.plano == plano_filme:
                  print(f"Ver Filme {filme}")
                elif self.plano == "Premium":
                  print(f"Não vai poder ver o filme {filme}")
                elif self.plano == "Basic" and plano_filme == "Premium":
                    print("faça upgrade para premium para ver este filme")
                else:
                  print("Plano Invalido!")


cliente = Cliente("cohla", "cohla@gmail.com", "Premium")
print(cliente.plano)
cliente.ver_filme("Harry Potter", "Premium")

cliente.mudar_plano("Basic")
print(cliente.plano)
cliente.ver_filme("Harry Potter", "Premium")
