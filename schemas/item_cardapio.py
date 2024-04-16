from pydantic import BaseModel
from typing import Optional, List

from model.item_cardapio import ItemCardapio
from model.categoria_cardapio import CategoriaCardapio

class ItemCardapioSchema(BaseModel):
    """ 
    Define como um novo item do cardápio a ser inserido 
    deve ser representado
    """     
    nome: str = "Refrigerante"
    descricao: str = "Coca-cola, Guaraná, Fanta e Sprite"
    preco: float = 12.50
    categoria_id: int = 1    

class ItemCardapioViewSchema(BaseModel):
    """ 
    Define como o item será retornado na listagem 
    dos Itens do Cardapio
    """
    nome: str = "Refrigerante"
    descricao: str = "Coca-cola, Guaraná, Fanta e Sprite"
    preco: float = 12.50

class ItemCardapioBuscaSchema(BaseModel):
    """ 
    Define como deve ser a estrutura que representa a busca. 
    Que será feita apenas com base no id do item do cardápio.
    """
    id: int = 1

class ItemCardapioDelSchema(BaseModel):
    """ 
    Define como deve ser a estrutura do dado retornado após uma requisição
    de remoção.
    """
    mesage: str
    id: int         

class ItemCardapioAddSchema(BaseModel):
    """ 
    Define como um novo item do cardápio a ser inserido 
    deve ser representado
    """
    nome: str = "Refrigerante"
    descricao: str = "Coca-cola, Guaraná, Fanta e Sprite"
    preco: float = 12.50
    categoria_id: int = 1            

def apresenta_novo_item_cardapio(item: ItemCardapio):
    """ Retorna uma representação do novo item do cardapio
    """
    return {
        "id": item.id,
        "nome": item.nome,
        "descricao": item.descricao,
        "preco": item.preco,
        "categoria_id": item.categoria_id       
    }  

     