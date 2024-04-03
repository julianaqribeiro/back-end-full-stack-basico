from pydantic import BaseModel
from typing import Optional, List

from model.item_cardapio import ItemCardapio


class ItemCardapioSchema(BaseModel):
    """ 
    Define como um novo item do cardápio a ser inserido 
    deve ser representado
    """
    nome: str = "Refrigerante"
    descricao: str = "Coca-cola, Guaraná, Fanta e Sprite"
    preco: float = 12.50
    categoria: int = 1  

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

class ItemCardapioViewSchema(BaseModel):
    """ 
    Define como o item será retornado: item + categoria.
    """
    nome: str = "Refrigerante"
    descricao: str = "Coca-cola, Guaraná, Fanta e Sprite"
    preco: float = 12.50    
    categoria: int = 1    


class ItemCardapioSemCategoriaViewSchema(BaseModel):
    """ 
    Define como o item será retornado na listagem 
    dos Itens do Cardapio
    """
    nome: str = "Refrigerante"
    descricao: str = "Coca-cola, Guaraná, Fanta e Sprite"
    preco: float = 12.50        


def apresenta_item_cardapio(item: ItemCardapio):
    """ 
    Retorna uma representação do item seguindo o schema 
    definido em ItemCardapioViewSchema.
    """
    return {
        "id": item.id,
        "nome": item.nome,
        "descricao": item.descricao,
        "preco": item.preco,
        "categoria": item.categoria      
    }    