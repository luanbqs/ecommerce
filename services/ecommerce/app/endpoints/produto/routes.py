from app import app

from werkzeug.routing import Rule

app.add_url_rule('/criar-produto'    , methods=['POST'], endpoint='/criar-produto')
app.add_url_rule('/procurar-produtos', methods=['POST'], endpoint='/procurar-produtos')
app.add_url_rule('/deletar-produto'  , methods=['POST'], endpoint='/deletar-produto')
app.add_url_rule('/editar-produto'   , methods=['POST'], endpoint='/editar-produto')
