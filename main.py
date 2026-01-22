from fasthtml.common import *
from componentes import gerar_titulo, gerar_formulario, gerar_lista_tarefas

app, routes = fast_app(static_dir="static")

lista_tarefas = []

@routes("/")
def homepage():
    formulario = gerar_formulario()
    elemento_lista_tarefa = gerar_lista_tarefas(lista_tarefas)
    return Titled("Lista de Tarefas 📘", Link(rel="stylesheet", href="/static/css/style.css"), formulario, elemento_lista_tarefa)

@routes('/adcionar_tarefa', methods=["post"])
def adcionar_tarefa(tarefa: str):
    if tarefa:
        lista_tarefas.append(tarefa)
    return gerar_lista_tarefas(lista_tarefas)

@routes("/deletar/{posicao}")
def deletar(posicao: int):
    if len(lista_tarefas) > posicao:
        lista_tarefas.pop(posicao)
    return gerar_lista_tarefas(lista_tarefas)

serve()