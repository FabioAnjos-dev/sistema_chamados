from chamado import Chamado

class SistemaChamados:
    def __init__(self):
        self.chamados = []
        self.proximo_id = 1

    def abrir_chamado(self, solicitante, titulo, descricao):
        chamado = Chamado(
        self.proximo_id,
        solicitante,
        titulo, 
        descricao
        )
        self.chamados.append(chamado)
        self.proximo_id += 1
        print("Chamado aberto com sucesso!")
        print(f"Numero do chamado: {chamado.id}")

    def listar_chamados(self):
        if not self.chamados:
            print("Nenhum chamado registrado.")


            print("\n=== CHAMADOS ===")
            for chamado in self.chamados:
                chamado.exibir()

                def buscar_chamado(self, id):
                    for chamado in self.chamados:
                        if chamado.id == id:
                            return chamado
                    return None

    def alterar_status(self, id, novo_status):
        chamado = self.buscar_chamado(id)
        if chamado is None:
            print("\nChamado não encontrado.")
            chamado.alterar_status(novo_status)
            print("\nStatus atualizado com sucesso!")

            def fechar_chamado(self, id):          
                chamado = self.buscar_chamado(id)
                if chamado is None:
                    print("\nChamado não encontrado.")
                    chamado.alterar_status('FECHADO')
                    print("\nChamado fechado com sucesso!")


            

        
        
            
      
