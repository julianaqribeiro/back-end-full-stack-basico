from typing import List
from pydantic import BaseModel

from model.categoria_cardapio import CategoriaCardapio
from schemas.item_cardapio import ItemCardapioViewSchema


class CategoriaCardapioSchema(BaseModel):
    """ 
    Define como uma nova categoria de cardapio a ser inserido 
    deve ser representado
    """
    id: int = 1
    nome: str = "Bebida"


class CategoriaCardapioComItensSchema(BaseModel):
    """ Define a representacao da categoria de cardapio com os itens vinculados 
    """
    nome: str = "Bebida",
    itens: List[ItemCardapioViewSchema]


class ListagemCategoriaCardapioComItensSchema(BaseModel):
    """ Define a representacao das categorias de cardapio com os itens vinculados 
    """
    categorias: List[CategoriaCardapioComItensSchema]


class ListagemCategoriasCardapioSchema(BaseModel):
    """ Define como uma listagem de categorias de cardapio será retornada.
    """
    categorias:List[CategoriaCardapioSchema]    

def apresenta_categorias_cardapio(categorias: List[CategoriaCardapio]):
    """ Retorna uma representação da listagem das categoria de cardapio
    """
    result = []
    for categoria in categorias:
        result.append({
            "id": categoria.id,
            "nome": categoria.nome                      
        })

    return {"categorias": result}

def apresenta_categorias_cardapio_com_itens(categorias: List[CategoriaCardapio]):
    """ 
    Retorna uma listagem das categorias de cardapio com todos os itens
    vinculados
    """    
    result = []
    for categoria in categorias:

        result.append({
            "nome": categoria.nome, 
            "itens": [{"id": item.id, "nome": item.nome, "descricao": item.descricao, "preco": ("R$ %.2f"%(item.preco)) } for item in categoria.itens]                    
        })

    return {"categorias": result}   