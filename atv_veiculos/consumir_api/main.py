import requests

if __name__ == '__main__':
    while True:
        opcao = input('1 - Listar todos os veiculos\n2 - Cadastrar um veiculo\n3 - Deletar um veiculo\n4 - Sair\nDigite uma opção:')
        if opcao == '1':
            r = requests.get('http://127.0.0.1:8000/veiculos')
            veiculos = r.json()
            if len(veiculos) == 0:
                print('\nNão há veiculos cadastrados\n')
            else:
                print('')
                for veiculo in veiculos:
                    print(f'| Nome: {veiculo['nome']} | Marca: {veiculo['marca']} | Modelo: {veiculo['modelo']} | Placa:{veiculo['placa']}')
                print('')
        elif opcao == '2':
            nome = input('Digite o nome do veiculo:')
            marca = input('Digite a marca do veiculo:')
            modelo = input('Digite o modelo do veiculo:')
            placa = input('Digite a placa do veiculo:')
            veiculo = {
                'nome':nome,
                'marca':marca,
                'modelo':modelo,
                'placa':placa
                }
            
            r = requests.post('http://127.0.0.1:8000/veiculos',json=veiculo)
            if r.status_code == 200:
                print('\nveiculo cadastrado com sucesso\n')
            else:
                print('Erro')

        elif opcao == '3':
            nome = input('Digite o nome do veiculo:')
            r = requests.get(f'http://127.0.0.1:8000/veiculos')
            if r.status_code == 200:
                r = requests.delete(f'http://127.0.0.1:8000/veiculos/{nome}')
                print(f'\n veiculo deletado com sucesso\n')
            else:
                print('\nveiculo não encontrado\n')

        elif opcao == '4':
            print('\nSaindo...\n')
            break
        else:
            pass