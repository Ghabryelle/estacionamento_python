import sqlite3

class Veiculo:
    def conexao(self):
        conexao = sqlite3.connect("estacionamento_db")
        consulta = conexao.cursor()
        tabela = """
        CREATE TABLE IF NOT EXISTS veiculos(
            id INTEGER PRIMARY KEY,
            placa VARCHAR(100),
            modelo VARCHAR(100),
            data_entrada DATE,
            horario_entrada TIME,
            data_saida DATE,
            horario_saida TIME
        );
        """

        consulta.execute(tabela)
        return conexao
    
    def cadastrarVeiculo(self, id, placa, modelo, data_entrada, horario_entrada, data_saida, horario_saida):
        conexao = self.conexao()

        sql = "INSERT INTO veiculos VALUES(?,?,?,?,?,?,?)" 

        campos = (id, placa, modelo, data_entrada, horario_entrada,  data_saida, horario_saida)

        consulta = conexao.cursor()
        consulta.execute(sql, campos)

        conexao.commit()

        print(consulta.rowcount, " linha inserida com sucesso\n")
        conexao.close()

    def consultarVeiculo(self):
        conexao = self.conexao()
        consulta = conexao.cursor()
        
        sql = "SELECT * FROM veiculos"
        consulta.execute(sql)
        
        resultado = consulta.fetchall()
        
        for itens in resultado:
            print(f"Id: {itens[0]}")
            print(f"Placa: {itens[1]}")
            print(f"Modelo: {itens[2]}")
            print(f"Data de entrada: {itens[3]}")
            print(f"Horario de entrada: {itens[4]}")
            print(f"Data de saida: {itens[5]}")
            print(f"Horario de saida: {itens[6]}")
            print("-"*40)
            
        conexao.close()
        

    def deletarVeiculo(self):
        conexao = self.conexao()
        consulta = conexao.cursor()
        
        id = int(input("Informe o id do veiculo que deseja excluir: "))
        
        sql = "DELETE FROM veiculos WHERE id = ?"
        
        campos = (id,)
        
        consulta.execute(sql, campos)
        conexao.commit()
        print(consulta.rowcount, " linha deletada com sucesso")
        
        if consulta.rowcount == 0:
            print("Esse ID não foi encontrado.\n")
        else:
            conexao.close() 
        
    def atualizarVeiculo(self):
        conexao = self.conexao()
        consulta = conexao.cursor()
        
        id = input("Digite o ID que deseja alterar: ")
        placa = input("Nova placa: ")
        modelo = input("Novo modelo: ")
        data_entrada = input("Nova data de entrada: ")
        horario_entrada = input("Nova hora de entrada: ")
        data_saida = input("Nova data de saída: ")
        horario_saida = input("Nova hora de saída: ")
        
        sql = "UPDATE veiculos SET placa = ?, modelo = ?, data_entrada = ?, horario_entrada = ?, data_saida = ?, horario_saida = ? WHERE id = ?"
        
        campos = (placa, modelo, data_entrada, horario_entrada, data_saida, horario_saida, id)
        
        consulta.execute(sql, campos)
        conexao.commit()
        print(consulta.rowcount, " linha atualizada com sucesso\n")
        conexao.close() 
        
    def consultarVeiculoIndividual (self):
        conexao = self.conexao()
        consulta = conexao.cursor()

        id = int(input("Informe o ID do veículo que deseja consultar: "))

        sql = "SELECT * FROM veiculos WHERE id = ?"
        campos = (id,)
        consulta.execute(sql, campos)

        resultado = consulta.fetchall()

        for itens in resultado:
            print(f"ID: {itens[0]}")
            print(f"Placa: {itens[1]}")
            print(f"Modelo: {itens[2]}")
            print(f"Data de Entrada: {itens[3]}")
            print(f"Horario de Entrada: {itens[4]}")
            print(f"Data de Saida: {itens[5]}")
            print(f"Horario de Saida: {itens[6]}")
        conexao.close()
