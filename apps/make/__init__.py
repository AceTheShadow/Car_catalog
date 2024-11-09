from flask import Blueprint

blueprint = Blueprint(
    'make_blueprint',
    __name__,
    url_prefix='/admin/make'
)
