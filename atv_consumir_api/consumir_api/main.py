import requests

if __name__ == '__main__':
    while True:
        opcao = input('1 - Listar todos os livros\n2 - Pesquisar um Livro pelo título\n3 - Cadastrar um livro\n4 - Deletar um livro\n5 - Editar um livro\n6 - Sair\nDigite uma opção:')
        if opcao == '1':
            r = requests.get('http://127.0.0.1:8000/livros')
            livros = r.json()
            if len(livros) == 0:
                print('\nNão há livros cadastrados\n')
            else:
                print('')
                for livro in livros:
                    print(f'| Título: {livro['titulo']} | Ano: {livro['ano']} | Edição: {livro['edicao']} |')
                print('')
        elif opcao == '2':
            titulo = input('Digite o título do livro:')
            r = requests.get(f'http://127.0.0.1:8000/livros/{titulo}')
            if r.status_code == 404:
                print('\nLivro indisponível\n')
            else:
                livro = r.json()
                print(f'\n| Título: {livro['titulo']} | Ano: {livro['ano']} | Edição: {livro['edicao']} |\n')
        elif opcao == '3':
            titulo = input('Digite o título do livro:')
            ano = input('Digite o ano do livro:')
            edicao = input('Digite a edição do livro:')
            livro = {
                'titulo':titulo,
                'ano':int(ano),
                'edicao':int(edicao)
            }
            r = requests.post('http://127.0.0.1:8000/livros',json=livro)
            if r.status_code == 200:
                print('\nLivro cadastrado com sucesso\n')
            else:
                print('Erro')
        elif opcao == '4':
            titulo = input('Digite o título do livro:')
            r = requests.get(f'http://127.0.0.1:8000/livros/{titulo}')
            if r.status_code == 200:
                r = requests.delete(f'http://127.0.0.1:8000/livros/{titulo}')
                print(f'\n Livro deletado com sucesso\n')
            else:
                print('\n Livro não encontrado\n')
        elif opcao == '5':
            titulo = input('Digite o título do livro:')
            r = requests.get(f'http://127.0.0.1:8000/livros/{titulo}')
            if r.status_code == 404:
                print('\nLivro indisponível\n')
            else:
                livro = r.json()
                print('DADOS DO LIVRO:')
                print(f'\n| Título: {livro['titulo']} | Ano: {livro['ano']} | Edição: {livro['edicao']} |\n')

                novo_titulo = input('Digite o novo título:')
                novo_ano = input('Digite o novo ano:')
                novo_edicao = input('Digite a nova edição:')
                livro_editado = {
                    'titulo': novo_titulo,
                    'ano': int(novo_ano),
                    'edicao': int(novo_edicao)
                }
                r = requests.put(f'http://127.0.0.1:8000/livros/{titulo}', json=livro_editado)
                print('\nLivro editado com sucesso.\n')
                
        elif opcao == '6':
            print('\nSaindo...\n')
            break
        else:
            pass
    
