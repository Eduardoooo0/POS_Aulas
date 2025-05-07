from fastapi import FastAPI, HTTPException
from models import Usuario, Livro, Biblioteca, Emprestimo
from typing import List

app = FastAPI()


usuarios: List[Usuario] = []
livros: List[Livro] = []
bibliotecas: List[Biblioteca] = []
emprestimos: List[Emprestimo] = []



@app.get('/usuarios', response_model=List[Usuario])
def listar_usuarios():
    return usuarios


@app.get('/livros', response_model=List[Livro])
def listar_livros():
    return livros


@app.get('/bibliotecas', response_model=List[Biblioteca])
def listar_bibliotecas():
    return bibliotecas

@app.get('/emprestimos', response_model=List[Emprestimo])
def listar_emprestimos():
    return emprestimos



@app.post('/usuarios/', response_model=Usuario)
def cadastrar_usuarios(usuario:Usuario):
    usuarios.append(usuario)
    return usuario


@app.post('/livros/', response_model=Livro)
def cadastrar_livros(livro:Livro):
    livros.append(livro)
    return livro


@app.post('/bibliotecas/', response_model=Biblioteca)
def cadastrar_bibliotecas(biblioteca:Biblioteca):
    bibliotecas.append(biblioteca)
    return biblioteca

@app.post('/emprestimos/', response_model=Emprestimo)
def cadastrar_emprestimos(emprestimo:Emprestimo):
    emprestimos.append(emprestimo)
    return emprestimo


@app.delete('/usuarios/{user_nome}', response_model=Usuario)
def excluir_usuarios(user_nome:str):
    for index,user in enumerate(usuarios):
        if user.username == user_nome:
            del usuarios[index]
            return user
    raise HTTPException(status_code=404, detail='não localizado')

@app.delete('/livros/{livro_nome}', response_model=Livro)
def excluir_livros(livro_nome:str):
    for index,livro in enumerate(livros):
        if livro.titulo == livro_nome:
            del livros[index]
            return livro
    raise HTTPException(status_code=404, detail='não localizado')

@app.delete('/bibliotecas/{blibioteca_nome}', response_model=Biblioteca)
def excluir_bibliotecas(biblioteca_nome:str):
    for index,biblioteca in enumerate(bibliotecas):
        if biblioteca.nome == biblioteca_nome:
            del bibliotecas[index]
            return biblioteca
    raise HTTPException(status_code=404, detail='não localizado')

@app.delete('/emprestimos/{user_nome}', response_model=Emprestimo)
def excluir_emprestimos(user_nome:str):
    for index,emprestimo in enumerate(emprestimos):
        if emprestimo.usuario.username == user_nome:
            del emprestimos[index]
            return emprestimo
    raise HTTPException(status_code=404, detail='não localizado')