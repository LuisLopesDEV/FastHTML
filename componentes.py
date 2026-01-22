from fasthtml.common import Div, H1, P, Form, Input, Button, Ul, Li, A, Fieldset, Group, Grid

colors = [Input(type='color', value=o) for o in ('#e66465', '#53d2c5', '#f6b73c')]

def gerar_titulo(titulo, subtitulo):
    return Div(
        H1(titulo),
        P(subtitulo),
        P('Esse componente foi Gerado com FastHTML')
    )

def gerar_formulario():
    formulario = Form(
            Group(
                Input(
                    type='text',
                    name='tarefa',
                    placeholder='Tarefa',),
                Button('Adcionar')),
            Grid(*colors),
        method='post',
        action='/adcionar_tarefa',
        hx_post='/adcionar_tarefa',
        hx_target='#lista-tarefa',
        hx_swap='outerHTML'
    )
    return formulario

def gerar_lista_tarefas(lista_tarefas):

    itens_lista = [Li(tarefa, ' - ', A("Excluir",
                                       hx_get=f'/deletar/{i}',
                                       hx_target='#lista-tarefa',
                                       hx_swap='outerHTML')) for i, tarefa in enumerate(lista_tarefas)]

    lista = Ul(
        *itens_lista, id='lista-tarefa'
    )
    return lista