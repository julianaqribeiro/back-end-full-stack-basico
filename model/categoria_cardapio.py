import json
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from model.base import Base
from model.item_cardapio import ItemCardapio

class CategoriaCardapio(Base):
    __tablename__ = 'categoria_cardapio'

    id = Column("pk_categoria_cardapio", Integer, primary_key=True, comment="Identificador da Categoria do Cardápio")
    nome = Column(String(200), unique=True, comment="Nome da Categoria do Cardápio", nullable=False)
    itens = relationship("ItemCardapio")
        
    def __init__(self, id: int, nome:str):
        """
        Cria uma Categoria de Cardápio

        Arguments:
            nome: nome da categoria de cardápio          
        """
        self.id = id
        self.nome = nome

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)        
        
