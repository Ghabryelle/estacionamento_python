import time 
from estacionamento import Veiculo

v1 = Veiculo()

while True:
    res = input("1 - Cadastrar \n2 - Consultar \n3 - Deletar \n4 - Atualizar \n5 - Consulta individual \n0 - Finalizar \n \nDigite qual opção deseja: ")
    if res == '1':
        id = input("ID: ")
        placa = input("Placa: ")
        modelo = input("Modelo: ")
        data_entrada = input("Data de entrada: ")
        horario_entrada = input("Horario de entrada: ")
        data_saida = input("Data de saída: ")
        horario_saida = input("Horario de saída: ")
            
        v1.cadastrarVeiculo(id, placa, modelo, horario_entrada, data_entrada, horario_saida, data_saida)
        
    elif res == '2':
        print("Consultando...\n")
        time.sleep(3)
        v1.consultarVeiculo()  
    elif res == '3':  
        v1.deletarVeiculo()
    elif res == '4':  
        v1.atualizarVeiculo()
    elif res == '0':
        print("Saindo...")  
        time.sleep(2)
        break
    elif res == '5':
        v1.consultarVeiculoIndividual()
    elif res > '5':
        print("Não tem essa opção.")