import requests

if __name__ == '__main__':
    while True:
        opcao = int(input('1 - Listar todos os livros\n2 - Pesquisar um Livro pelo título\n3 - Adicionar um livro\n4 - Deletar um livro\nDigite uma opção:'))
        if opcao == 1:
            r = requests.get('http://127.0.0.1:8000/livros')
            for i in r.text:
                dados = i[0]["titulo"]
                print(dados)
            break
        
        livro = {
            "titulo": "python",
            "ano":2024,
            "edicao":1
        }
        r = requests.post('http://127.0.0.1:8000/livros',json=livro)
        print(f'post : {r.status_code}')
        print(r.text)

        pesquisa = {
            "titulo":"python"
        }
        r = requests.get(f'http://127.0.0.1:8000/livros/{pesquisa["titulo"]}',)
        print(f'get único : {r.status_code}')
        print(r.text)

        r = requests.delete(f'http://127.0.0.1:8000/livros/{pesquisa["titulo"]}',)
        print(f'delete : {r.status_code}')
    
