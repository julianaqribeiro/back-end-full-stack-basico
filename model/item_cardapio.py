from sqlalchemy import Column, Float, ForeignKey, Numeric, String, Integer

from model.base import Base

class ItemCardapio(Base):
    __tablename__ = 'item_cardapio'
    
    id = Column(Integer, primary_key=True, autoincrement=True, comment="Identificador do Item do Cardápio")
    nome = Column(String(200), unique=True, comment="Nome do Item do Cardápio", nullable=False)
    descricao = Column(String(1000), comment="Descrição do Item  do Cardápio", nullable=False)
    preco = Column(Numeric(precision=3, scale=2), comment="Preço do Item  do Cardápio", nullable=False)    
    categoria_id = Column(Integer, ForeignKey("categoria_cardapio.pk_categoria_cardapio"), nullable=False, comment="Identificador da Categoria do Cardápio")        

    def __init__(self, nome:str, descricao:str, preco: Float, categoria_id:int):
        """
        Cria um Item do Cardapio
        
        Arguments:
            nome: nome do item do cardapio. 
            descricao: descricao do item do cardapio. 
            preco: preco do item do cardapio.    
            categoria: categoria a qual o item pertence       
        """
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.categoria_id = categoria_id            