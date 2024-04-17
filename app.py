from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session
from logger import logger
from model.categoria_cardapio import CategoriaCardapio
from model.item_cardapio import ItemCardapio
from schemas import *
from flask_cors import CORS

info = Info(title="API Módulo Full Stack Básico", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
categoria_cardapio_tag = Tag(name="CategoriaCardapio", description="Visualização de categorias do cardápio")
itens_cardapio_tag = Tag(name="ItensCardapio", description="Adição e remoção dos itens do cardápio à base")
cardapio_tag = Tag(name="Cardapio", description="Visualizacao do cardapio")


@app.get('/', tags=[home_tag])
def home():
    return redirect('/openapi')

@app.get('/categorias_cardapio', tags=[categoria_cardapio_tag],
         responses={"200": ListagemCategoriasCardapioSchema, "404": ErrorSchema})
def get_categorias_cardapio():
    """
    Pesquisa todas as Categorias de Cardápio cadastradas.
    Retorna uma representação da listagem de categorias.
    """
    logger.debug(f"Coletando categorias ")
    session = Session()
    categorias = session.query(CategoriaCardapio).order_by(CategoriaCardapio.nome.asc()).all()

    if not categorias:
        return {"categorias": []}, 200
    else:
        logger.debug(f"%d Categorias encontrados" % len(categorias))
        print(categorias)
        return apresenta_categorias_cardapio(categorias), 200


@app.post('/item_cardapio', tags=[itens_cardapio_tag],
          responses={"200": ItemCardapioAddSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_item_cardapio(form: ItemCardapioSchema):
    """
    Adiciona um novo Item do Cardápio à base de dados
    Retorna uma representação dos itens do cardapio.
    """
    item = ItemCardapio(
        nome=form.nome,
        descricao=form.descricao,
        preco=form.preco,
        categoria_id=form.categoria_id)
    
    logger.debug(f"Adicionando item de nome: '{item.nome}'")
    try:
        session = Session()
        session.add(item)
        session.commit()
        logger.debug(f"Adicionado item de nome: '{item.nome}'")
        return apresenta_novo_item_cardapio(item), 200

    except IntegrityError as e:
        error_msg = "Item do Cardápio de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar item '{item.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:       
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar item '{item.nome}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.delete('/item_cardapio', tags=[itens_cardapio_tag],
            responses={"200": ItemCardapioDelSchema, "404": ErrorSchema})
def del_item_cardapio(query: ItemCardapioBuscaSchema):        
    """ 
    Deleta um Item do cardapio a partir do id do item informado
    Retorna uma mensagem de confirmação da remoção. 
    """   
    item_id = query.id
    print(item_id)    
    logger.debug(f"Deletando dados sobre item #{str(item_id)}")
    session = Session()
    count = session.query(ItemCardapio).filter(ItemCardapio.id == item_id).delete()    
    session.commit()
        
    if count:
        logger.debug(f"Deletado produto #{str(item_id)}")
        return {"mesage": "item removido", "id": str(item_id)}
    else:
        error_msg = "Item não encontrado na base :/"
        logger.warning(f"Erro ao deletar o item #'{str(item_id)}', {error_msg}")
        return {"mesage": error_msg}, 404


@app.get('/cardapio', tags=[cardapio_tag],
         responses={"200": ListagemCategoriaCardapioComItensSchema, "404": ErrorSchema})
def get_cardapio():
    """
    Faz a busca por todos os Itens do Cardapio cadastrados
    Retorna uma representação do cardápio
    """
    logger.debug(f"Coletando itens ")
    session = Session()
    categorias = session.query(CategoriaCardapio).order_by(CategoriaCardapio.nome.asc()).all()

    if not categorias:
        return {"categorias": []}, 200
    else:
        logger.debug(f"%d itens encontrados" % len(categorias))
        print(categorias)
        return apresenta_categorias_cardapio_com_itens(categorias), 200


if __name__ == "__main__":
    app.run(debug=True)
